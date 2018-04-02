"""
AWS Lambda Function

  Description
"""

import json
import logging
import boto3


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('function_name')

AWS_REGION='eu-west-1'


def lambda_handler(event, context):
    """ Lambda Handler, entry to Lambda Function

        Args:
            event: json payload that triggers lambda function.
            context: Useful information about the execution environment.

        Returns:
            Nothing

        Raises:
            nothing
    """

    print("Lambda")


def get_instances_by_tag(client, tag_pair):
    """ Gets instances based on tag
        
        Args:
            client: boto3 client to use.
            tag_par: dict describing tag to use.
                Should follow pattern:
                {'Key': 'key_name', 'Value': 'value'}

        Returns:
            list of instance IDs with matching tag pattern
    """

    instances = client.describe_instances(Filters=filters)

    return instances['Reservations'][0]['Instances']
