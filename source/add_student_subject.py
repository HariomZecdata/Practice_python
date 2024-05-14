"""
imort database module
"""

import common.database as db  #import  database module
import common.execute_query as eq #import execute_query module

MYDB , MYCURSOR = db.establish_connection() # start database connection

#sql query for insert data into student_subject table
SQL = "insert into stusub (stuid,subid) values(9,5)"

#Access class 
OBJ =  eq.ExecuteQuery(MYDB , MYCURSOR)
OBJ.add_data(SQL)


# database connection close
db.close_connection(MYDB , MYCURSOR)
