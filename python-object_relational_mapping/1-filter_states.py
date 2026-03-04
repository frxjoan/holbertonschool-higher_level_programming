#!/usr/bin/python3
'''
This script connects to a MySQL database
and retrieves all states from the 'states' table
where the name starts with 'N' (upper N)
The database credentials are provided as command-line arguments.
'''
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM  states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
