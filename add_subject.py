"""
import database module
"""
import database as db  #import  database file

MYDB , MYCURSOR = db.establish_connection() #start database connection

#sql query for insert data into subjects table
SQL = "INSERT INTO subjects (subname) VALUES ('TOC')"

#insert data in databse using add_data function
db.add_data(MYDB, MYCURSOR, SQL)

# database connection close
db.close_connection(MYDB , MYCURSOR)
