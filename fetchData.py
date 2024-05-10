import database as db

sql = "SELECT *FROM STUDENT"

x=db.getData(sql)

for ele in x:
    print(ele)
