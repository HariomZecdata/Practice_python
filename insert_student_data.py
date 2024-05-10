import database as db #import  database file


#sql query for insert data into student table
sql = "INSERT INTO STUDENT (Name, Age, Address) VALUES ('Yash ASATI', 23, 'Ratlam')"

#insert student data in database
db.add_data(sql)
