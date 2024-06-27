import mysql.connector

# Ensure you provide the correct parameters to connect via TCP/IP
try:
    conn = mysql.connector.connect(
        host="localhost",  # Replace with your host, if different
        user="root",
        password="komi",  # Replace with your actual root password
        database="your_database"   # Replace with the database you want to connect to
    )

    cursor = conn.cursor()

    # Example query: fetch all states from a 'states' table
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

