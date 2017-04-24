from flask import Flask
import os
import requests

app = Flask(__name__)

def send_simple_message():
    return requests.post(
        f"https://api.mailgun.net/v3/{os.environ['MAILGUN_DOMAIN_NAME']}/messages",
        auth=("api", os.environ['MAILGUN_API_KEY']),
        data={"from": "some one <no-reply@minodi.com>",
              "to": [os.environ['MAILGUN_RECEIVER_EMAIL']],
              "subject": "Hello from minodi",
              "text": "Testing some Mailgun awesomness!"})

@app.route("/api/hello", methods=['POST'])
def hello():
    send_simple_message()
    return "hello"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)

