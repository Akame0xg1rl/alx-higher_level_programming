#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query using parameterized query to fetch states
        sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(sql_query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print each state tuple in the format (id, name)
        for row in results:
            print(row)

        # Disconnect from server
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

