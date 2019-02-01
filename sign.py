import boto3

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# Your Bucket Name
bucket = s3.Bucket('alex-react-coin')

# Gets the list of objects in the Bucket
s3_Bucket_iterator = bucket.objects.all()

# IGenerates the Signed URL for each object in the Bucket


def sign_urls_and_list():
    for i in s3_Bucket_iterator:
        url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={
            'Bucket': bucket.name, 'Key': i.key}, ExpiresIn=60)
        print(url)
    return 'List made successfully'
