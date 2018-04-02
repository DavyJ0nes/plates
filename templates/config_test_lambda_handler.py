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
        """ sets up 3 mock VPCs to test with and tags them """

        self.client = boto3.client('ec2', region_name='us-west-1')

        for i in range(1, 4):
            cidr_range = "192.168.{}.0/24".format(i)
            vpc_response = self.client.create_vpc(
                CidrBlock=cidr_range
            )

            self.client.create_tags(
                Resources=[
                    vpc_response['Vpc']['VpcId']
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

    
    def test_get_vpcs(self):
        """ Tests that the get_vpc function works as expected """

        self.vpcs = lambda_handler.get_vpcs(self.client)

        # The first entry here is the default VPC that is mocked out by default in moto
        wanted_vpc_cidr_list = ["172.31.0.0/16", "192.168.1.0/24", "192.168.2.0/24", "192.168.3.0/24"]

        # Check that mocking is set up correctly by doing a simple compaision on the expected cidr blocks
        for vpc in self.vpcs:
            self.assertIn(vpc['CidrBlock'], wanted_vpc_cidr_list)
