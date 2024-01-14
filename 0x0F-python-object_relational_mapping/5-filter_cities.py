#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.name FROM cities
                 JOIN states ON states.id=cities.state_id
                WHERE states.name LIKE %s""", (argv[4],))
    rows = curs.fetchall()
    print(", ".join(row[0] for row in rows))
    curs.close()
    db.close()
