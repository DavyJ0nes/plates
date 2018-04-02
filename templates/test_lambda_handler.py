"""
test_lambda_handler
    Test Suite for <id> AWS Lambda Function
"""

from src import lambda_handler
import re
import unittest
import boto3
from moto import mock_ec2


@mock_ec2
class TestLambdaHandler(unittest.TestCase):

    def setUp(self):
        """ sets up mock infrastructure to test with """

        self.client = boto3.client('ec2', region_name='us-west-1')

        ec2_response = self.client.run_instances(
                MaxCount=1,
                MinCount=1,
                ImageId='ami-1234abcd',
                InstanceType='t2-micro',
        )

        # Register Instance ID as Class Variable
        self.test_instance_id = ec2_response['Instances'][0]['InstanceId']

        self.client.create_tags(
            Resources=[
                self.test_instance_id
            ],
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'Production',
                },
                {
                    'Key': 'Test',
                    'Value': 'True',
                },
            ],
        )


    def tearDown(self):
        """ function that runs after the test suite has been run """
        pass

    
    def test_get_instances_by_tag(self):
        """ Tests that the get_instance function works as expected """

        tag_pair = {
                'Key': 'Test',
                'Value': 'True',
        }

        instances = lambda_handler.get_instances_by_tag(self.client, tag_pair)

        self.assertGreater(len(instances), 0)
        self.assertEqual(instances[0], self.test_instance_id)

