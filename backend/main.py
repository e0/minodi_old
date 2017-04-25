from flask import Flask, request
import os
import requests

app = Flask(__name__)

def send_simple_message(content):
    return requests.post(
        f"https://api.mailgun.net/v3/{os.environ['MAILGUN_DOMAIN_NAME']}/messages",
        auth=("api", os.environ['MAILGUN_API_KEY']),
        data={"from": "some one <no-reply@minodi.com>",
              "to": [os.environ['MAILGUN_RECEIVER_EMAIL']],
              "subject": "Hello from minodi",
              "text": content})

@app.route("/api/hello", methods=['POST'])
def hello():
    payload = request.get_json(silent=True)
    send_simple_message(repr(payload))
    return "hello back"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)

