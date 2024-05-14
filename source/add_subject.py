"""
import database module
"""
import common.database as db  #import  database file
import common.execute_query as eq

MYDB , MYCURSOR = db.establish_connection() #start database connection

#sql query for insert data into subjects table
SQL = "INSERT INTO subjects (subname) VALUES ('TOC')"

#Object of ExecuteQuery Class
OBJ = eq.ExecuteQuery(MYDB , MYCURSOR)
OBJ.add_data(SQL)

# database connection close
db.close_connection(MYDB , MYCURSOR)
