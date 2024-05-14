"""
import pandas module 
import database module
"""

import pandas as pd
import database as db

#file_path: /home/hp/Downloads/salaries (2).csv
df = pd.read_csv(r"/home/hp/Downloads/salaries (2).csv")

MYDB , MYCURSOR = db.establish_connection()

for row in df.iterrows():
    DATA_TUPLE = tuple(row)  # Convert the row to a tuple
    SQL_QUERY = "INSERT INTO salaries VALUES" # Define your SQL INSERT query
    SQL_QUERY += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) {DATA_TUPLE}"
    # Execute the SQL query with the data tuple
    db.add_data(MYDB, MYCURSOR , SQL_QUERY)
#close connection
db.close_connection(MYDB , MYCURSOR)
