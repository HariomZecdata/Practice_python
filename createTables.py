import database as db 

# db.mycursor.execute("CREATE TABLE STUDENT(ID INT NOT NULL AUTO_INCREMENT,NAME VARCHAR(20) NOT NULL,AGE INT NOT NULL, ADDRESS CHAR (25),  PRIMARY KEY (ID))")




try:
    # db.mycursor.execute("create table subjects(id INT NOT NULL AUTO_INCREMENT ,subname VARCHAR (20)  ,PRIMARY KEY (id))")
    # db.mycursor.execute("create table stusub(stuid INT, subid INT, FOREIGN KEY (stuid) REFERENCES STUDENT(ID), FOREIGN KEY (subid) REFERENCES subjects(id) )")
     
     

    print(db.mycursor)

except Exception as e:
    print(e)
 