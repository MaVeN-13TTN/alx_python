import MySQLdb
def list_states(username, password, database):
    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    # Create a cursor to execute queries
    cursor = connection.cursor()
    # Execute the query to list all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # Fetch the results
    results = cursor.fetchall()
    # Print the results
    for row in results:
        print(row[0], row[1])
    # Close the cursor and connection
    cursor.close()
    connection.close()
if __name__ == "__main__":
    # Get the MySQL username, password, and database name from the user
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter MySQL database name: ")
    # List all states
    list_states(username, password, database)