#INTENTIONALLY INSECURE EXAMPLE FOR TESTING SCANNERS ONLY
#NEVER use or commit real credentials like this.

from flask import Flask, jsonify
import boto3

#FAKE AWS CREDENTIALS FORMATTED TO BE DETECTABLE
AWS_ACCESS_KEY_ID = 'AKIAIOSFODNN7EXAMPLE'
AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
AWS_SESSION_TOKEN = 'IQoJb3JpZ2luX2VjECoaCXVzLWVhc3QtMSoFAkK0BBCtGk527D/PjT3R6pTfPCdJpZYbFp4/bLzaf8PjT3R6pTfPCdJpZYbFp4/bLzaf8bFp4/bLzaf8='

APP_CONFIG = {
    'aws': {
        'accessKeyId': 'AKIATESTING123456789',
        'secretAccessKey': 'aBcDeFgHiJkLnMOPqRsTuVwXyZ123456789aBcDeFgH',
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