"""
 import Database  module 

"""

import database as db

# connection establish for DB
MYDB, MYCURSOR = db.establish_connection()


#sql query for insert data into student table
SQL = "INSERT INTO STUDENT (Name, Age, Address) VALUES ('Gopal ASATI', 23, 'Ratlam')"


#insert student data in database using add_data function
db.add_data(MYDB, MYCURSOR ,SQL)
