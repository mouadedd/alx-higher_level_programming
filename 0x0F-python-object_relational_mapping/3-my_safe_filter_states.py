#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table 'hbtn_0e_0_usa'
where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
