"""
AWS Config Rule <ID>

  Description
"""

import json
import logging
import boto3


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('rule_id')

# Specify desired resource types to validate
APPLICABLE_RESOURCES = ["AWS::EC2::VPC"]
IS_MOCK_TEST=False
AWS_REGION='eu-west-1'


def find_violation(tags, rule_parameters):
    """ Get useful message about the type of violation if any.
        Note that this function will need to change based on the type of rule being implemented

        Args:
            tags: list of tags (this is arbitary)
            rule_parameters: dict of the AWS config rules provided to the lambda

        Returns:
            violation: string describing violation. If there is no violation then returns None

        Raises:
            Nothing
    """

    # This is just for template purpose
    if 1 > 2:
        violation = "violation: resouce does not have access"

    if violation == "":
        return None
    return  violation


def evaluate_compliance(configuration_item, rule_parameters, applicable_resources):
    """ Checks resource compliance based on AWS Config
        Args:
            configuration_item: dict describing resource to check
            rule_parameters: dict of the AWS config rules provided to the lambda
            applicable_reources: list of AWS Resources that this rule applies to

        Returns:
            dictionary describing compliance to be used by the put_evaluations

        Raises:
            Nothing
    """

    if configuration_item["resourceType"] not in applicable_resources:
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The rule doesn't apply to resources of type " +
            configuration_item["resourceType"] + "."
        }

    if configuration_item["configurationItemStatus"] == "ResourceDeleted":
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The configurationItem was deleted and therefore cannot be validated."
        }

    current_tags = configuration_item["configuration"].get("tags")
    violation = find_violation(current_tags, rule_parameters)        

    if violation:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": violation
        }

    return {
        "compliance_type": "COMPLIANT",
        "annotation": "This resource is compliant with the rule."
    }


def lambda_handler(event, context):
    """ Lambda Handler, entry to Lambda Function

        Args:
            event: json payload that triggers lambda function.
            context: Useful information about the execution environment.

        Returns:
            evaluation dictionary if is being tested

        Raises:
            nothing
    """

    if context is 'MOCK_TEST':
        IS_MOCK_TEST=True

    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    config_rule_name = invoking_event['configRuleName']
    resource_id = invoking_event['configurationItem']['resourceId']
    rule_parameters = json.loads(event['ruleParameters'])

    LOGGER.info("Lambda Called by {}".format(config_rule_name))

    evaluation = evaluate_compliance(configuration_item, rule_parameters, APPLICABLE_RESOURCES)

    if IS_MOCK_TEST:
        return evaluation

    config = boto3.client("config", region_name=AWS_REGION)

    if evaluation["compliance_type"] is not 'COMPLIANT':
        LOGGER.warn("Resource ID: {} is not compliant".format(resource_id))

    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]

    LOGGER.info('Sending AWS Config Evaluations')
    config.put_evaluations(
        Evaluations=[
            {
                "ComplianceResourceType":
                    configuration_item["resourceType"],
                "ComplianceResourceId":
                    configuration_item["resourceId"],
                "ComplianceType":
                    evaluation["compliance_type"],
                "Annotation":
                    evaluation["annotation"],
                "OrderingTimestamp":
                    configuration_item["configurationItemCaptureTime"]
            },
        ],
        ResultToken=result_token
    )