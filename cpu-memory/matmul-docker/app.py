from flask import Flask, request, jsonify
import threading
import numpy as np
from time import time
import json
import gc

app = Flask(__name__)



def matmul(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    start = time()
    C = np.matmul(A, B)
    latency = time() - start

    # Memory cleanup
    del A
    del B
    del C
    gc.collect()

    return latency

def matmul_task(data):
    request_json = data
    number = int(request_json["number"])
    request_uuid = request_json['uuid']
    start_time = time()

    latency = matmul(number)

    return {
        "statusCode": 200,
        "body": {
            'latency': latency,
            'start_time': start_time,
            'uuid': request_uuid,
            'number': number,
            'test_name': 'matmul'
        }
    }

def process_matmul_thread(data):
    result = matmul_task(data)
    return result

@app.route('/matmul', methods=['POST'])
def process_matmul():
    data = request.json
    result = process_matmul_thread(data)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

