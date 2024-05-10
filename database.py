import mysql.connector  # Import the MySQL Connector module

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345",  
        database="products"
    )

    if mydb.is_connected():
        print("Connected to the database")
        # Further operations can be performed here
    else:
        print("Failed to connect to the database")
    # Connection successful, proceed with your code...
    mycursor = mydb.cursor()



    #get data from databse
    def get_data(sql):
        try:

            #execute sql query
            mycursor.execute(sql)

            #fetch all the row from database
            myresult = mycursor.fetchall()
            if len(myresult)==0:
                return None
            else:
                return myresult
        except Exception as e:
            print(e)
        finally:
            if mydb.is_connected():

                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")
                  



    # Create table 
    def create_table(sql):
        try:

            #execute sql query
            mycursor.execute(sql)
            print("Table created successfully")
        except Exception as e:
            print(e)
        finally:
            if mydb.is_connected():

                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")



    # Insert row into table
    def add_data(sql):
        try:

            #execute sql query
            mycursor.execute(sql)

            #commit changes
            mydb.commit()
            print("Data inserted successfully") 
        except Exception as e:
            print("Error:", e)
            mydb.rollback()
        finally:
            if mydb.is_connected():

                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")



except mysql.connector.Error as error:
    print("Error while connecting to MySQL:", error)





