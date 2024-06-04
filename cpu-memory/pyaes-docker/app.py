from flask import Flask, request, jsonify
import threading
from time import time
import random
import string
import pyaes
import json
import gc

app = Flask(__name__)

def generate(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def pyaes_encrypt_decrypt(length_of_message, num_of_iterations):
    message = generate(length_of_message)
    # 128-bit key (16 bytes)
    KEY = b'\xa1\xf6%\x8c\x87}_\xcd\x89dHE8\xbf\xc9,'
    start = time()
    
    for _ in range(num_of_iterations):
        aes = pyaes.AESModeOfOperationCTR(KEY)
        ciphertext = aes.encrypt(message)
        aes = pyaes.AESModeOfOperationCTR(KEY)
        plaintext = aes.decrypt(ciphertext)
        aes = None

    latency = time() - start

    # Memory cleanup
    del aes
    gc.collect()

    return latency

def pyaes_task(data):
    request_json = data
    length_of_message = int(request_json["length_of_message"])
    num_of_iterations = int(request_json["num_of_iterations"])
    request_uuid = request_json['uuid']
    start_time = time()

    latency = pyaes_encrypt_decrypt(length_of_message, num_of_iterations)

    return {
        "statusCode": 200,
        "body": {
            'latency': latency,
            'length_of_message': length_of_message,
            'num_of_iterations': num_of_iterations,
            'start_time': start_time,
            'uuid': request_uuid,
            'test_name': 'pyaes'
        }
    }

def process_pyaes_thread(data):
    result = pyaes_task(data)
    return result

@app.route('/pyaes', methods=['POST'])
def process_pyaes():
    data = request.json
    result = process_pyaes_thread(data)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

