import database as db  #import  database file


try:
 
    #sql query for create student table 
    student = "CREATE TABLE STUDENT(ID INT NOT NULL AUTO_INCREMENT,NAME VARCHAR(20) NOT NULL,AGE INT NOT NULL, ADDRESS CHAR (25),  PRIMARY KEY (ID))"
  
    #create table from database using create_table function
    db.create_table(student)

    #sql query for create subject table
    subject = "create table subjects(id INT NOT NULL AUTO_INCREMENT ,subname VARCHAR (20)  ,PRIMARY KEY (id))"

    #crete table from databse using create_table function
    db.create_table(subject)

    #sql query for create student_subject table
    student_subject = "create table stusub(stuid INT, subid INT, FOREIGN KEY (stuid) REFERENCES STUDENT(ID), FOREIGN KEY (subid) REFERENCES subjects(id) )"
    
    #create table from database using create_table function
    db.create_table()
     


except Exception as e:
    print(e)
 