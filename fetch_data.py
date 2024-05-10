import database as db  #import  database file


#sql query for select data from STUDENT table
sql = "SELECT * FROM STUDENT"

#fetch data from database
x = db.get_data(sql)

#print data
for ele in x:
    print(ele)
