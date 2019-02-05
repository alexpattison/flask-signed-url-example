from flask import Flask, request, redirect
import sign
import jwt
import os

app = Flask(__name__)

secret = os.environ['SECRET']


@app.route('/')
def pull_url():
    encoded = request.args.get('token')
    decoded = jwt.decode(encoded, secret, algorithms=['HS256'])
    generated_url = sign.generate_presigned_url(decoded)
    return redirect(generated_url)


if __name__ == '__main__':
    app.run()
