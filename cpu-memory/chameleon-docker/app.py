from flask import Flask, request, jsonify
from time import time
import six
import json
from chameleon import PageTemplate
import gc

app = Flask(__name__)

BIGTABLE_ZPT = """\
<table xmlns="http://www.w3.org/1999/xhtml"
xmlns:tal="http://xml.zope.org/namespaces/tal">
<tr tal:repeat="row python: options['table']">
<td tal:repeat="c python: row.values()">
<span tal:define="d python: c + 1"
tal:attributes="class python: 'column-' + %s(d)"
tal:content="python: d" />
</td>
</tr>
</table>""" % six.text_type.__name__

def generate_html_table(num_of_rows, num_of_cols, request_uuid):
    start_time = time()

    tmpl = PageTemplate(BIGTABLE_ZPT)

    data = {}
    for i in range(num_of_cols):
        data[str(i)] = i

    table = [data for x in range(num_of_rows)]
    options = {'table': table}

    rendered_data = tmpl.render(options=options)
    latency = time() - start_time

    # Cleaning up large objects
    del data
    del table
    del options
    del rendered_data
    gc.collect()  # Force garbage collection

    return {
        "latency": latency,
        "start_time": start_time,
        "uuid": request_uuid,
        "num_of_rows": num_of_rows,
        "num_of_cols": num_of_cols,
        "test_name": "chameleon"
    }

@app.route('/generate-table', methods=['POST'])
def generate_table():
    data = request.json
    num_of_rows = data['num_of_rows']
    num_of_cols = data['num_of_cols']
    request_uuid = data['uuid']
    
    result = generate_html_table(num_of_rows, num_of_cols, request_uuid)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

