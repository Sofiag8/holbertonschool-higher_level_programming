#!/usr/bin/python3
""" script that takes in the name of a state as an
argument (SQL injection free) and lists all cities
of that state, using the database hbtn_0e_4_usa """

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
    cmd = """ SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id = states.id WHERE states.name=%s
    ORDER BY cities.id ASC """
    cur.execute(cmd, (search,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    data_base.close()
