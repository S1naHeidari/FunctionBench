from flask import Flask, request, jsonify
from urllib.request import urlopen
from time import time
import json
import threading
import gc

app = Flask(__name__)

def json_dumps_loads(link):
    start = time()
    f = urlopen(link)
    data = f.read().decode("utf-8")
    network = time() - start

    start = time()
    json_data = json.loads(data)
    str_json = json.dumps(json_data, indent=4)
    latency = time() - start

    # Memory cleanup
    del json_data
    del str_json
    gc.collect()

    return latency

def json_dumps_loads_task(data):
    request_json = data
    link = request_json["link"]
    request_uuid = request_json['uuid']
    start_time = time()

    latency = json_dumps_loads(link)

    return {
        "statusCode": 200,
        "body": {
            'latency': latency,
            'start_time': start_time,
            'uuid': request_uuid,
            'test_name': 'json-dumps-loads'
        }
    }

def process_json_dumps_loads_thread(data):
    result = json_dumps_loads_task(data)
    return result

@app.route('/json-dumps-loads', methods=['POST'])
def process_json_dumps_loads():
    data = request.json
    result = process_json_dumps_loads_thread(data)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

