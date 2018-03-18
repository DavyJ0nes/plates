"""
boto_script_test.py
    Test Script for Boto using moto
"""

import boto_script
import boto3
from moto import mock_s3

EXPECTED_KEYS = ['key1', 'key2']


@mock_s3
def bucket_setup():
    """test bucket stubbing"""
    # Set up S3 as we expect it to be
    s3resource = boto3.resource('s3', region_name='us-west-1')
    test_bucket = s3resource.create_bucket(Bucket='bucket_name')
    for name in EXPECTED_KEYS:
        test_bucket.put_object(
            Body=b'abcdefghi',
            Key=name
        )

    return test_bucket


@mock_s3
def test_get_bucket_objects():
    """testing get_bucket_objects function"""
    print('testing get_bucket_objects')
    bucket_setup()
    s3resource = boto3.resource('s3', region_name='us-west-1')

    # Now call the actual function
    keys = boto_script.get_bucket_objects(s3resource, 'bucket_name')
    assert EXPECTED_KEYS == [k.key for k in keys]
    print('test passed')
    print('-----------')


@mock_s3
def test_main():
    """
    testing main function
    other wise known as happy path
    """
    print('testing main')
    bucket_setup()
    s3resource = boto3.resource('s3', region_name='us-west-1')

    # Now call the actual function
    bucket_objects = boto_script.get_bucket_objects(s3resource, 'bucket_name')
    print(bucket_objects)


if __name__ == "__main__":
    test_main()
