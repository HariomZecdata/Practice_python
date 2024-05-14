"""
Import  Database module 
"""


import database as db  #import  database file


MYDB, MYCURSOR = db.establish_connection()

#sql query for select data from STUDENT table
SQL = "SELECT * FROM STUDENT"

#fetch data from database
x = db.get_data(MYCURSOR , SQL)

#print data
for ele in x:
    print(ele)

# database connection close
db.close_connection(MYDB , MYCURSOR)
