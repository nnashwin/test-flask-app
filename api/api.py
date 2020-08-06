import json
import os
import time
from flask import Flask, request, make_response
import flask

import sqlite3

app = Flask(__name__, static_folder='../build', static_url_path='/')

FLASK_DIR=os.path.dirname(os.environ['FLASK_APP'])
DB_PATH=f"{FLASK_DIR}/files.db"

def appendHeaders(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'

# Static path for application
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/files',methods = ['POST', 'GET'])
def handle_files_json():
    conn = sqlite3.connect(DB_PATH)
    if request.method == 'POST':
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO files(id, data) values (?, ?)',
            ['1', toJson(strList)])
        conn.commit()
        conn.close()

        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return {'files': val}
    else:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('select * from files')
        result = c.fetchone()
        for row in result:
            decoded_data = json.loads(row)

        resp = make_response(decoded_data)
        # only allowing cors due to this being a demo
        # In actual production application will limit based on demand
        appendHeaders(resp)
        return resp

