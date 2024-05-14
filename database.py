"""
Database module for interacting with MySQL database.
"""

import sys
import mysql.connector

MYDB = MYCURSOR = None

def establish_connection():
    """
    Establishes connection to MySQL database.

    Returns:
        tuple: Tuple containing database connection object and cursor object.
    """
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="12345",
            database="products"
        )

        if mydb.is_connected():
            print("Connected to the database")
            mycursor = mydb.cursor()
            return mydb, mycursor
        print("Failed to connect to the database")
        sys.exit(1)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        sys.exit(1)

# In the __main__ block:
MYDB, MYCURSOR = establish_connection()


def get_data(mycursor, sql):
    """
    Retrieves data from database based on the provided SQL query.

    Args:
        mycursor: Cursor object for executing SQL queries.
        sql (str): SQL query to retrieve data.

    Returns:
        list: List of tuples containing the retrieved data.
    """
    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            return None
        return myresult
    except mysql.connector.Error as e:
        print("Error:", e)
        return None

def create_table(mycursor, sql):
    """
    Creates a table in the database based on the provided SQL query.

    Args:
        mycursor: Cursor object for executing SQL queries.
        sql (str): SQL query to create table.
    """
    try:
        mycursor.execute(sql)
        print("Table created successfully")
    except mysql.connector.Error as e:
        print("Error:", e)

def add_data(mydb, mycursor, sql):
    """
    Inserts data into a table in the database based on the provided SQL query.

    Args:
        mydb: Database connection object.
        mycursor: Cursor object for executing SQL queries.
        sql (str): SQL query to insert data.
    """
    try:
        mycursor.execute(sql)
        mydb.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as e:
        print("Error:", e)
        mydb.rollback()

def close_connection(mydb, mycursor):
    """
    Closes the database connection.

    Args:
        mydb: Database connection object.
        mycursor: Cursor object.
    """
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    MYDB, MYCURSOR = establish_connection()

    # Example SQL queries
    CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS example_table (name VARCHAR(255))"
    ADD_DATA_SQL = "INSERT INTO example_table (name) VALUES ('John')"
    GET_DATA_SQL = "SELECT * FROM example_table"

    # Create table
    create_table(MYCURSOR, CREATE_TABLE_SQL)

    # Insert data
    add_data(MYDB, MYCURSOR, ADD_DATA_SQL)
    # Retrieve data
    result = get_data(MYCURSOR, GET_DATA_SQL)
    print("Retrieved data:", result)

    close_connection(MYDB, MYCURSOR)
