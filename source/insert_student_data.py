"""
 import Database  module 

"""

import common.database as db
import common.execute_query as eq

def insert_data_fun():
    # connection establish for DB
    MYDB, MYCURSOR = db.establish_connection()

    #object of ExecuteQuery Class
    OBJ = eq.ExecuteQuery(MYDB , MYCURSOR)

    #sql query for insert data into student table
    SQL = "INSERT INTO STUDENT (Name, Age, Address) VALUES ('Priyanshu', 23, 'Ratlam')"


    #insert student data in database using add_data function
    OBJ.add_data(SQL)

    # database connection close
    db.close_connection(MYDB , MYCURSOR)

    return True
