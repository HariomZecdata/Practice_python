class ExecuteQuery:
    def __init__(self, mydb, mycursor):
        self.mydb = mydb 
        self.mycursor = mycursor
    
    def get_data(self, sql):
        """
        Retrieves data from database based on the provided SQL query.

        Args:
        sql (str): SQL query to retrieve data.

        Returns:
        list: List of tuples containing the retrieved data.
        """
        try:
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()
            if len(myresult) == 0:
                return None
            return myresult
        except Exception as  e:
            print("Error:", e)
            return None
    
    def create_table(self , sql):
        """
        Creates a table in the database based on the provided SQL query.

        Args:
        mycursor: Cursor object for executing SQL queries.
        sql (str): SQL query to create table.
        """
        try:
            self.mycursor.execute(sql)
            print("Table created successfully")

        except Exception as e:
            print("Error:", e)
    
    def add_data(self , sql):
        """
        Inserts data into a table in the database based on the provided SQL query.

        Args:
        mydb: Database connection object.
        mycursor: Cursor object for executing SQL queries.
        sql (str): SQL query to insert data.
        """
        try:
            self.mycursor.execute(sql)
            self.mydb.commit()
            print("Data inserted successfully")
        except Exception as e:
            print("Error:", e)
            self.mydb.rollback()
    