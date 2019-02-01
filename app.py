from flask import Flask, request, redirect
import sign

app = Flask(__name__)


@app.route('/')
def pull_url():
    key = request.args.get('key')
    generated_url = sign.generate_presigned_url(key)
    return redirect(generated_url)
