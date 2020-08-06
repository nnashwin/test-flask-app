import csv
import json
import sqlite3

from parsenames import toJson

strList = []
with open('data/names.csv') as dataFile:
    spamreader = csv.reader(dataFile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(row)
        strList += row


sortedList = strList.sort()
conn = sqlite3.connect('files.db')
c = conn.cursor()
try:
    c.execute('DROP TABLE files')
except sqlite3.OperationalError:
    print('table did not exist, could not drop table, but will still create table.')

c.execute('CREATE TABLE files (id varchar(3) UNIQUE, data json)')
c.execute('INSERT OR REPLACE INTO files(id, data) values (?, ?)',
        ['1', toJson(strList)])
conn.commit()
conn.close()
