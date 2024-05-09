import database as db

sql = "INSERT INTO STUDENT (Name, Age, Address) VALUES (%s, %s, %s)"
values = ('Rinkesh ASATI', 29, 'BHOPAL')

try:
    db.mycursor.execute(sql, values)
    db.mydb.commit()
    print(db.mycursor.rowcount, "record inserted.")
except Exception as e:
    print("Error:", e)
    db.mydb.rollback()

