import csv
import database as db
file_path = '/home/hp/Downloads/general-city-budget-incremental-changes.csv'



# sql= "CREATE TABLE Student_Satisfaction_Survey (Department_Code VARCHAR(100),Department_Name VARCHAR(255),Program_Code VARCHAR(100),Program_Name VARCHAR(255),Fund_Code VARCHAR(20),Fund_Name VARCHAR(255),Source_Fund_Code VARCHAR(20),Source_Fund_Name VARCHAR(255),Budget_Request_Description VARCHAR(255),Budget_Request_Category VARCHAR(255),Account_Code VARCHAR(130),Account_Name VARCHAR(255),One_Time_Or_On_going VARCHAR(255),Budget VARCHAR(255),Incremental_Change VARCHAR(255))"
# db.createTable(sql)


try:
    
    with open(file_path,mode ='r')as file:
         
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


