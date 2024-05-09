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
    # Continue with your operations...
      
    #   create table 
    # res = mycursor.execute("CREATE TABLE customers (firstname VARCHAR(20), lastname VARCHAR(20),address VARCHAR(255))")
    # print(res)


except mysql.connector.Error as err:
    print("Error:", err)



