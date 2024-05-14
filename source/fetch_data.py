import common.database as db
from common.execute_query import ExecuteQuery 
import pytest

# Establish connection to the database
MYDB, MYCURSOR = db.establish_connection()

# Object of ExecuteQuery class
OBJ = ExecuteQuery(MYDB , MYCURSOR)

# SQL query to select data from the STUDENT table
SQL = "SELECT * FROM STUDENT"

# Execute the query and fetch data
RES = OBJ.get_data(SQL)

# Print fetched data
for row in RES:
    print(row)

# Close the database connection
db.close_connection(MYDB, MYCURSOR)
