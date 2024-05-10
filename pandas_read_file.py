import pandas as pd
import database as db
df = pd.read_csv(r"/home/hp/Downloads/salaries (2).csv")

try:
    for row in df.iterrows():
        data_tuple = tuple(row)  # Convert the row to a tuple
        
        # Define your SQL INSERT query
        sql_query = "INSERT INTO salaries VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Execute the SQL query with the data tuple
        db.mycursor.execute(sql_query, data_tuple)

    # Commit the changes 
    db.mydb.commit()    
    print("All the records inserted successfully")

except Exception as e:
    print("Error:", e)
    db.mydb.rollback()


