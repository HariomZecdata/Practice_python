import mysql.connector  # Import the MySQL Connector module

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345",  # Replace with your actual password
        database="products"
    )
    if mydb.is_connected():
        print("Connected to the database")
        # Further operations can be performed here
    else:
        print("Failed to connect to the database")
    # Connection successful, proceed with your code...
    mycursor = mydb.cursor()
  # create table 
    def createTable(sql):
        try:
            mycursor.execute(sql)
            print("Table Create successfully")
        except Exception as e:
             print(e)

    #Insert row into table
    def addData(sql):
        try:
           mycursor.execute(sql)
           mydb.commit()
           print("Data inserted successfully") 
        except Exception as e:
            print("Error:", e)
            mydb.rollback()

         

    #fetch data from table     
    def getData(sql):
        try:
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print("Error:", e)

except mysql.connector.Error as err:
    print("Error:", err)



