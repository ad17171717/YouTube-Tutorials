#INTENTIONALLY INSECURE EXAMPLE FOR TESTING SCANNERS ONLY
#NEVER use or commit real credentials like this.

from flask import Flask, jsonify
import boto3

#fake AWS credentials
AWS_ACCESS_KEY_ID = 'AKIA1234567890ABCD'
AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
AWS_SESSION_TOKEN = 'IQoJb3JpZ2luX2VjECoaCXVzLWVhc3QtMSoEFAKEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

APP_CONFIG = {
    'aws': {
        'accessKeyId': 'AKIAFAKEKEYID123456',
        'secretAccessKey': 'abcdEFGHijklMNOPqrstUVWXyz0123456789abcdFAKE',
        'region': 'us-east-1',
    },
    'app': {'name': 'toy-webapp', 'debug': False},
}

app = Flask(__name__)

@app.route('/')
def index():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=APP_CONFIG['aws']['region'],
    )
    _ = s3
    return jsonify(
        {
            'status': 'ok',
            'note': 'toy app with FAKE keys for TruffleHog testing',
            'detectors_expected': ['AWS Access Key', 'AWS Secret Key', 'Session Token'],
        }
    )

if __name__ == '__main__':
    #behaves like a mini web app
    app.run(host='127.0.0.1', port=5000, debug=False)
