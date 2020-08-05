import json
import time
from flask import Flask, request

import sqlite3

app = Flask(__name__, static_folder='../build', static_url_path='/')

DB_PATH='./files.db'

# Static path for application
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/time',methods = ['POST', 'GET'])
def get_current_time():
    conn = sqlite3.connect(DB_PATH)
    if request.method == 'POST':
        c = conn.cursor()
        val = 'cookies' + time.asctime()
        c.execute("insert or replace into files(id, data) values (?, ?)",
                ['100', json.dumps({'time': val})])
        conn.commit()
        conn.close()
        return {'time': val}
    else:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('select * from files')
        result = c.fetchone()
        for row in result:
            print(row)
            decoded_data = json.loads(row)
        return decoded_data

