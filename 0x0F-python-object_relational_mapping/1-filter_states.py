#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
with a name starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name
                 LIKE 'N%' ORDER BY states.id")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
