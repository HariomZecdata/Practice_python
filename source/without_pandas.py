"""
import csv module 
import database module
"""
import csv
import common.database as db
import common.execute_query as eq

# File path
FILE_PATH = '/home/hp/Downloads/general-city-budget-incremental-changes.csv'

# Establish database connection
MYDB, MYCURSOR = db.establish_connection()

#Object of ExecuteQuery Class from execute_query module
OBJ = eq.ExecuteQuery(MYDB , MYCURSOR )

try:
    with open(FILE_PATH, mode='r', encoding='utf-8') as file:
        CSV_FILE = csv.reader(file)
        for line in CSV_FILE:
            # Adjust this line based on the number of columns in your CSV file
            SQL_QUERY = "INSERT INTO Student_Satisfaction_Survey VALUES "
            SQL_QUERY += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) {line}"
            OBJ.add_data(SQL_QUERY)
except FileNotFoundError:
    print("File not found.")
