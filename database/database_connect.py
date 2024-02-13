import MySQLdb
import json

import settings

def db_connect():
    # Connect to db
    db = MySQLdb.connect(host=settings.DB_HOST,
                        user=settings.DB_USER,
                        passwd=settings.DB_PASSWORD,
                        db=settings.DB_NAME)

    cursor = db.cursor()
    return cursor, db

def execute_get_queries(query):
    cursor, db = db_connect()
    # Execute SQL query
    cursor.execute(query)

    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rows = cursor.fetchall()
    json_data=[]

    # Convert response from db to json format
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))

    # Close the connection
    db.close()
    return json_data

def execute_put_queries(query):

    cursor,db = db_connect()

    # Execute SQL query
    cursor.execute(query)

    # Commit changes 
    db.commit()

    db.close()
    return 200