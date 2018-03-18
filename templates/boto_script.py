#!/user/bin/env python3
"""
boto_script
  Python script for interacting with AWS
  Example here is showing interacting with S3
"""

import argparse
import logging
import sys
import boto3


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('boto_script')


def main():
    """main function"""
    # Set up Command Line Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', action='store', dest='region', default='eu-west-1')
    parser.add_argument('--profile', action='store', dest='profile', default='default')
    parser.add_argument('--bucket-name', action='store', dest='bucket_name', required=True)
    parser.add_argument('--detailed-output', action='store_true', dest='detailed_output', default=False)
    parser.add_argument('--debug', action='store_true', dest='debug', default=False)
    args = parser.parse_args()

    # Set up Debug Logging
    if args.debug:
        LOGGER.setLevel(logging.DEBUG)

    # Set up boto Session Parameters
    session = boto3.Session(profile_name=args.profile, region_name=args.region)
    s3client = session.client('s3')
    s3resource = session.resource('s3')

    # Checking if bucket exists
    if args.bucket_name not in list_buckets(s3resource):
        print("Bucket: {} does not exist".format(args.bucket_name))
        sys.exit(1)

    LOGGER.debug('Getting buckets')
    bucket_objects = get_bucket_objects(s3resource, args.bucket_name)


def list_buckets(s3client):
    """lists buckets in region"""
    LOGGER.debug('Starting: list_buckets')
    bucket_list = []
    for bucket in s3client.buckets.all():
        bucket_list.append(bucket.name)

    return bucket_list


def get_bucket_objects(s3client, bucket_name):
    """gets objects from bucket"""
    LOGGER.debug('Starting: get_bucket_objects')
    bucket = s3client.Bucket(bucket_name)

    bucket_object_list = []
    for obj in bucket.objects.all():
        if not obj.key.endswith('/'):
            obj_fullinfo = s3client.Object(bucket_name, obj.key)
            bucket_object_list.append(obj_fullinfo)

    return bucket_object_list


if __name__ == "__main__":
    main()
