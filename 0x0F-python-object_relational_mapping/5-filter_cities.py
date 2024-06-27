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

        # Prepare SQL query using parameterized query to fetch cities of a specific state
        sql_query = """
                    SELECT GROUP_CONCAT(name SEPARATOR ', ')
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC
                    """

        # Execute the SQL query with the state_name parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch the result (single value since we used GROUP_CONCAT)
        result = cursor.fetchone()[0]

        # Print the result
        print(result)

        # Disconnect from server
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

