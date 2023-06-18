#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    query = """SELECT *
                FROM cities
                   INNER JOIN states
                  ON cities.state_id = states.id
                ORDER BY cities.id;"""

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        if city[2] == state:
            print(city[2])


if __name__ == "__main__":
    main()
