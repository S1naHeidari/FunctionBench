from flask import Flask, request, jsonify
import threading
import math
from time import time
import json
import gc

app = Flask(__name__)


def float_operations(n):
    start = time()
    for i in range(n):
        sin_i = math.sin(i)
        cos_i = math.cos(i)
        sqrt_i = math.sqrt(i)
    latency = time() - start

    # Memory cleanup
    gc.collect()

    return latency

def float_operations_task(data):
    request_json = data
    number = int(request_json["number"])
    request_uuid = request_json['uuid']
    start_time = time()

    latency = float_operations(number)

    return {
        "statusCode": 200,
        "body": {
            'latency': latency,
            'start_time': start_time,
            'uuid': request_uuid,
            'number': number,
            'test_name': 'float-operation'
        }
    }

def process_float_operations_thread(data):
    result = float_operations_task(data)
    return result

@app.route('/float-operations', methods=['POST'])
def process_float_operations():
    data = request.json
    result = process_float_operations_thread(data)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

