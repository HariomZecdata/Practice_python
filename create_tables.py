"""
import database module 

"""

import database as db

MYDB, MYCURSOR = db.establish_connection()

try:
    # SQL query for creating the student table
    STUDENT = "CREATE TABLE STUDENT(ID INT NOT NULL AUTO_INCREMENT, "
    STUDENT += "NAME VARCHAR(20) NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(25), PRIMARY KEY (ID))"
    # Create the student table
    db.create_table(MYCURSOR, STUDENT)

    # SQL query for creating the subject table
    SUBJECT = "CREATE TABLE SUBJECTS(ID INT NOT NULL AUTO_INCREMENT, "
    SUBJECT += "SUBNAME VARCHAR(20), PRIMARY KEY (ID))"
    # Create the subject table
    db.create_table(MYCURSOR, SUBJECT)

    # SQL query for creating the student_subject table
    STUDENT_SUBJECT = "CREATE TABLE STUSUB(STUID INT, SUBID INT, "
    STUDENT_SUBJECT += "FOREIGN KEY (STUID) REFERENCES STUDENT(ID),"
    STUDENT_SUBJECT += " FOREIGN KEY (SUBID) REFERENCES SUBJECTS(ID))"
    # Create the student_subject table
    db.create_table(MYCURSOR, STUDENT_SUBJECT)

except Exception as e:
    print("error message:", e)

# database connection close
db.close_connection(MYDB , MYCURSOR)
