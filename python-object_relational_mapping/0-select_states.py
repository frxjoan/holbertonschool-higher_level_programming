#!/usr/bin/python3
''' 
This script connects to a MySQL database
and retrieves all states from the 'states' table
ordered by their ID in ascending order
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
