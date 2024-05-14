"""
import database module
"""
import common.database as db

SQL = "INSERT INTO employee VALUES (%s, %s, %s)"
VALUE = ('Hariom Asati', '940000', '1')

MYDB, MYCURSOR = db.establish_connection()

def insert_data(mydb, mycursor, sql, value):
    """
    Inserts data into a table in the database based on the provided SQL query.

    Args:
        mydb: Database connection object.
        mycursor: Cursor object.
        sql: SQL insert query.
        value: Data for insert command.
    """
    try:
        # Update status of employee if employee exists
        update_query = "UPDATE employee SET status='0' WHERE name=%s AND status=%s"
        mycursor.execute(update_query, (value[0], value[2]))

        # Check if any rows were updated
        if mycursor.rowcount > 0:
            mycursor.execute(sql, value)
        else:
            print("No rows were updated, skippingg insertion.")

        # Permanent change to the database
        mydb.commit()
        print('Successfully data inserted')

    except Exception as e:
        print("An error occurred:", e)
        # Any error occurred, rollback database
        mydb.rollback()

if __name__ == "__main__":
    # Insert data
    insert_data(MYDB, MYCURSOR, SQL, VALUE)
   