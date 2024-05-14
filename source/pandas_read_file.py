"""
import pandas module 
import database module
"""

import pandas as pd
import common.database as db
import common.execute_query as eq

#file_path: /home/hp/Downloads/salaries (2).csv
df = pd.read_csv(r"/home/hp/Downloads/salaries (2).csv")

MYDB , MYCURSOR = db.establish_connection()

#Object of ExecuteQuery Class from execute_query module
OBJ = eq.ExecuteQuery(MYDB , MYCURSOR )

for row in df.iterrows():
    DATA_TUPLE = tuple(row)  # Convert the row to a tuple
    SQL_QUERY = "INSERT INTO salaries VALUES" # Define your SQL INSERT query
    SQL_QUERY += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) {DATA_TUPLE}"
    # Execute the SQL query with the data tuple
    OBJ.add_data(SQL_QUERY)
#close connection
db.close_connection(MYDB , MYCURSOR)
