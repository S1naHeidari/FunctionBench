from flask import Flask, request, jsonify
from numpy import matrix, linalg, random
from time import time
import threading
import json
import gc

app = Flask(__name__)

# Track active threads
active_threads = 0
lock = threading.Lock()

def increment_thread_count():
    global active_threads
    with lock:
        active_threads += 1

def decrement_thread_count():
    global active_threads
    with lock:
        active_threads -= 1

def linpack(n):
    # LINPACK benchmarks
    ops = (2.0 * n) * n * n / 3.0 + (2.0 * n) * n

    # Create AxA array of random numbers -0.5 to 0.5
    A = random.random_sample((n, n)) - 0.5
    B = A.sum(axis=1)

    # Convert to matrices
    A = matrix(A)
    B = matrix(B.reshape((n, 1)))

    # Ax = B
    start = time()
    x = linalg.solve(A, B)
    latency = time() - start

    mflops = (ops * 1e-6 / latency)

    # Memory cleanup
    del A
    del B
    del x
    gc.collect()

    result = {
        'mflops': mflops,
        'latency': latency
    }

    return result

def linpack_task(data):
    request_json = data
    number = int(request_json["number"])
    request_uuid = request_json['uuid']
    start_time = time()

    result = linpack(number)

    return {
        "statusCode": 200,
        "body": {
            **result,
            'start_time': start_time,
            'number': number,
            'uuid': request_uuid,
            'test_name': 'linpack'
        }
    }

def process_linpack_thread(data):
    increment_thread_count()
    try:
        result = linpack_task(data)
        return result
    finally:
        decrement_thread_count()

@app.route('/linpack', methods=['POST'])
def process_linpack():
    data = request.json
    result = process_linpack_thread(data)
    return jsonify(result), 200

@app.route('/threads', methods=['GET'])
def get_thread_count():
    return jsonify({"active_threads": active_threads}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

