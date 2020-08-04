import sqlite3

conn = sqlite3.connect('files.db')
c = conn.cursor()
c.execute("CREATE TABLE files (id varchar(3) UNIQUE, data json)")
conn.commit()
conn.close()
