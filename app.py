from flask import Flask
import boto3
import requests
import sign

app = Flask(__name__)

s3 = boto3.client('s3')

result = s3.get_bucket_policy(Bucket='alex-react-coin')
print(result)


@app.route('/')
def sign_and_list():
    list = sign.sign_urls_and_list()
    return list
