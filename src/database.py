import mysql.connector
from mysql.connector import Error, errorcode
import sql_queries

class Database:
    def __init__(self):
        self.context = None
        self.last_error = None

        self.db_name = "Projektarbeit"
        self.address = "localhost"
        self.username = "admin"
        self.password = "admin"


    #TODO: Maybe return a boolean value and check before if we have a valid connection?
    def establish_connection(self):
        try:
            if self.context == None:
                self.context = mysql.connector.connect(host=self.address, password=self.password, user=self.username, db=self.db_name, charset="utf8mb4")
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.last_error = "Verbindung mit der Datenbank fehlgeschlagen, nutzername oder password falsch."
                print("Verbindung mit der Datenbank fehlgeschlagen, nutzername oder password falsch.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.last_error = f"Die Datenbank '{self.db_name}' existiert nicht."
                print("Die Datenbank 'fuhrpark' existiert nicht.")
            else:
                self.last_error = f"{err}"
                print(err)

    def disconnect(self):
        self.context.close()
        self.context = None

    def insert_row(self, query_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return
        
        cursor = self.context.cursor()

        if data:
            cursor.execute(query_string, data)
            mietwagennr = cursor.lastrowid
            context.commit()

    def query_all_data(self, query_string):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()
    
        data = cursor.execute(query_string, ())
        return cursor

    def query_row(self, query_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()

        if data:
            cursor.execute(query_string, data)
        else:
            cursor.execute(query_string)
        pass

    def filter_row(self, query_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()
        cursor.execute(query_string, data)
        return cursor
    
    def update_row(self, update_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()

        if data:
            cursor.execute(update_string, data)
            context.commit()

    def delete_row(self, delete_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()

        if data:
            cursor.execute(delete_string, data)
            context.commit()
