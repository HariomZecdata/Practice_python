import pandas as pd
import database as db 

df = pd.read_csv(r"/home/hp/Downloads/salaries (2).csv")
print(df)

# try:
#     for row in df.iterrows():
#         data_tuple = tuple(row)  # Convert the row to a tuple
#     # Define your SQL INSERT query
#         sql_query = "INSERT INTO salaries VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"  
#     # Execute the SQL query with the data tuple
#         db.mycursor.execute(sql_query, data_tuple)

#     # Commit the changes 
#     db.mydb.commit()    
#     print("All the reacode inserted successully")
# except Exception as e:
#         print("Error:", e)
#         db.mydb.rollback()

# create table salaries
# sql="CREATE TABLE s
# alaries (work_year INT, experience_level VARCHAR(50), employment_type VARCHAR(50), job_title VARCHAR(100), salary INT, salary_currency VARCHAR(10),salary_in_usd INT, employee_residence VARCHAR(50), remote_ratio INT, company_location VARCHAR(50), company_size VARCHAR(10));"
# db.createTable(sql)

