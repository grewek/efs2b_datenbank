import mysql.connector
from mysql.connector import Error, errorcode

def establish_connection():
    try:
        context = mysql.connector.connect(host="localhost", password="admin", user="admin", db="fuhrpark", charset="utf8mb4")
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


context = establish_connection()
