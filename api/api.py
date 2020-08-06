import json
import os
import time
from flask import Flask, request

import sqlite3

app = Flask(__name__, static_folder='../build', static_url_path='/')

FLASK_DIR=os.path.dirname(os.environ['FLASK_APP'])
DB_PATH=f"{FLASK_DIR}/files.db"

print(FLASK_DIR)
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
        return {'files': val}
    else:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('select * from files')
        result = c.fetchone()
        for row in result:
            print(row)
            decoded_data = json.loads(row)
        return decoded_data

