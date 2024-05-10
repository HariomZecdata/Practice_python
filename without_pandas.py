import csv  #inport csv
import database as db #import  database file
file_path = '/home/hp/Downloads/general-city-budget-incremental-changes.csv'

try:
       
    with open(file_path,mode ='r')as file:  #open file
         
      csvFile = csv.reader(file)

      for lines in csvFile:

        data=tuple(lines)

        sql_query = "INSERT INTO Student_Satisfaction_Survey VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"  

        db.mycursor.execute(sql_query,data)

    # Commit the changes 
    
      db.mydb.commit()    
      print("All the reacode inserted successully")
except Exception as e:
        print("Error:", e)
        db.mydb.rollback()
