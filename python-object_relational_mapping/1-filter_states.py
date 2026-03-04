#!/usr/bin/python3
"""List all states from the database with names starting with 'N'."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and print all states with names starting with 'N'."""

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
