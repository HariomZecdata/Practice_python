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

    close_connection(MYDB, MYCURSOR)
