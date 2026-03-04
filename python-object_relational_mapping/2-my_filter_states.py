#!/usr/bin/python3
'''
This script connects to a MySQL database
and retrieves all states from the 'states' table
where the name matches the provided argument
The database credentials and state name are provided as command-line arguments.
'''
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (state_name,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
