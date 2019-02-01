import boto3
import os

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# Your Bucket Name
bucket = s3.Bucket(os.environ['BUCKET'])


def generate_presigned_url(key):
    url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={
        'Bucket': bucket.name, 'Key': key}, ExpiresIn=5)
    return url
