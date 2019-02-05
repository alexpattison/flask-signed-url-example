from flask import Flask, request, redirect
import sign
import jwt
import os

app = Flask(__name__)

secret = os.environ['SECRET']


@app.route('/')
def pull_url():
    encoded = request.args.get('token')
    if not encoded:
        return 'Please specify a token'
    else:
        decoded = jwt.decode(encoded, secret, algorithms=['HS256'])
        generated_url = sign.generate_presigned_url(decoded)
        print(generated_url)
        return redirect(generated_url)


if __name__ == '__main__':
    app.run()
