import boto3
from flask import Flask, request, redirect
import jwt
import os

app = Flask(__name__)

secret = os.environ['SECRET']

s3_client = boto3.client('s3')


def generate_presigned_url(jwt):
    url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={
        'Bucket': jwt['bucket'], 'Key': jwt['key']}, ExpiresIn=60)
    return url


@app.route('/')
def pull_url():
    print('new changes')
    encoded = request.args.get('token')
    decoded = jwt.decode(encoded, secret, algorithms=['HS256'])
    generated_url = generate_presigned_url(decoded)
    return redirect(generated_url)


if __name__ == '__main__':
    app.run()
