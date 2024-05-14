"""
import database module 

"""

import common.database as db
import common.execute_query as eq

MYDB, MYCURSOR = db.establish_connection()

# Object of ExecuteQuery class
OBJ = eq.ExecuteQuery(MYDB , MYCURSOR)

# SQL query for creating the student table
STUDENT = "CREATE TABLE STUDENT(ID INT NOT NULL AUTO_INCREMENT, "
STUDENT += "NAME VARCHAR(20) NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(25), PRIMARY KEY (ID))"

OBJ.create_table(STUDENT)

# SQL query for creating the subject table
SUBJECT = "CREATE TABLE SUBJECTS(ID INT NOT NULL AUTO_INCREMENT, "
SUBJECT += "SUBNAME VARCHAR(20), PRIMARY KEY (ID))"
# Create the subject table
OBJ.create_table(SUBJECT)

# SQL query for creating the student_subject table
STUDENT_SUBJECT = "CREATE TABLE STUSUB(STUID INT, SUBID INT, "
STUDENT_SUBJECT += "FOREIGN KEY (STUID) REFERENCES STUDENT(ID),"
STUDENT_SUBJECT += " FOREIGN KEY (SUBID) REFERENCES SUBJECTS(ID))"
# Create the student_subject table
OBJ.create_table(STUDENT_SUBJECT)

# database connection close
db.close_connection(MYDB , MYCURSOR)
