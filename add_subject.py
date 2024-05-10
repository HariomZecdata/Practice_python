import database as db  #import  database file


#sql query for insert data into subjects table
sql = "INSERT INTO subjects (subname) VALUES ('TOC')"

#insert data in databse using add_data function
db.add_data(sql)