import os
import mysql.connector

from flask import jsonify
from dateutil import parser

# Get the backup folder path from environment variable
sql_host = os.environ.get('SQL_HOST')
if sql_host is None or not sql_host:
    sql_host = 'localhost'


# Connect to the MySQL database
def dbconnect():
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="password",
        database="fca")


def log_to_db(action, parameter, status):
    db = dbconnect()
    cursor = db.cursor()

    insert_query = "INSERT INTO log (action, parameter, status) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (action, parameter, status))
    db.commit()

    cursor.close()
    db.close()
