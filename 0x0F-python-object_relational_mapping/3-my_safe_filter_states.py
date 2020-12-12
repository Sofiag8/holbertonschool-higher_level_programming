#!/usr/bin/python3
""" script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

SQL Injection  are known as as an attack vector for websites and databases

Setting up placeholders so that the database can fill in the data values
properly and safely.

Placeholder syntax depends on the database you are using
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    data_base = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                charset="utf8")
    cur = data_base.cursor()
    search = argv[4]
    cmd = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(cmd, (search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
