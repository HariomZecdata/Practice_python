import database as db  #import  database file


#sql query for insert data into student_subject table
sql = "insert into stusub (stuid,subid) values(9,5)"

#insert data in database usning add_add function
db.add_data(sql)

