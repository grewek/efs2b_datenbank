import mysql.connector
from mysql.connector import Error, errorcode
import sql_queries

def establish_connection():
    try:
        context = mysql.connector.connect(host="localhost", password="admin", user="admin", db="Projektarbeit", charset="utf8mb4")
        return context
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Verbindung mit der Datenbank fehlgeschlagen, nutzername oder password falsch.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Die Datenbank 'fuhrpark' existiert nicht.")
        else:
            print(err)

def disconnect(context):
    context.close()

def query_row(context, query_string, data):
    cursor = context.cursor()

    if data:
        cursor.execute(query_string, data)
    else:
        cursor.execute(query_string)
    pass

def update_row(context, update_string, data):
    pass

def delete_row(context, delete_string, data):
    pass

context = establish_connection()
query_row(context, sql_queries.query_all, None)

disconnect(context)
