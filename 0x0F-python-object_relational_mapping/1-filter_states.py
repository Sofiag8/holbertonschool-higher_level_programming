#!/usr/bin/python3
""" script that lists all states with a name starting with upper N """
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2],
                     db=argv[3], charset="utf8")
cur = db.cursor()
rows = cur.execute("SELECT * FROM states WHERE NAME like 'N%' ORDER BY id ASC")
for i in range(rows):
    result = cur.fetchone()
    print(result)
cur.close()
db.close()
