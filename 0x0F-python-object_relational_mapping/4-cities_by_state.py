#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

        # Prepare SQL query to fetch cities with corresponding state names
        sql_query = """
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC
                    """

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print each city tuple in the format (id, city_name, state_name)
        for row in results:
            print(row)

        # Disconnect from server
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

