import boto3

s3_client = boto3.client('s3')


def generate_presigned_url(jwt):
    url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={
        'Bucket': jwt['bucket'], 'Key': jwt['key']}, ExpiresIn=60)
    return url
