"""
imort database module
"""

import database as db  #import  database file

MYDB , MYCURSOR = db.establish_connection() # start database connection

#sql query for insert data into student_subject table
SQL = "insert into stusub (stuid,subid) values(9,5)"

#insert data in database usning add_add function
db.add_data(MYDB , MYCURSOR ,SQL)

# database connection close
db.close_connection(MYDB , MYCURSOR)
