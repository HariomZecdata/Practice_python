import database as db

sql = "SELECT *FROM STUDENT"

try:
    db.mycursor.execute(sql)
    myresult = db.mycursor.fetchall()
    for x in myresult:
        print(x)
   
except Exception as e:
    print("Error:", e)
