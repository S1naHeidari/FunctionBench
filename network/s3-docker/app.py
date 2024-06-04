from flask import Flask, request, jsonify
import boto3
from time import time
import json
from botocore.client import Config
import uuid
import os

app = Flask(__name__)

TMP_DIR = "/tmp/files"
if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)


def handle_s3_operation(data):
    request_json = data


    input_bucket = request_json["input_bucket"]
    object_key = request_json['object_key']
    output_bucket = request_json['output_bucket']
    key_id = request_json['key_id']
    access_key = request_json['access_key']
    request_uuid = request_json['uuid']
    start_time = time()
    
    s3_client = boto3.client('s3', endpoint_url='http://192.168.56.1:9000',
            aws_access_key_id=key_id,
            aws_secret_access_key=access_key,
            config=Config(signature_version='s3v4'))
    try:
        start_time = time()

        new_name = str(uuid.uuid4())
        path = os.path.join(TMP_DIR, new_name)

        start = time()
        s3_client.download_file(input_bucket, object_key, path)
        download_time = time() - start

        start = time()
        s3_client.upload_file(path, output_bucket, new_name)
        upload_time = time() - start

        return {
            "download_time": download_time,
            "upload_time": upload_time,
            "start_time": start_time,
            "uuid": request_uuid,
            "test_name": "s3-download-speed"
        }
    finally:
        if os.path.exists(path):
            os.remove(path)

@app.route('/s3-operation', methods=['POST'])
def s3_operation():
    data = request.json
    result = handle_s3_operation(data)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

