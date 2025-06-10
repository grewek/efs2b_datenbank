import mysql.connector
from mysql.connector import Error, errorcode
import sql_queries

#Datenbank Klasse die die Interaktion mit der Datenbank übernimmt
class Database:
    #Initalisiert ein neues Objekt der Klasse Datenbank, es setzt dabei alle nötigen Eigenschaften auf Defaultwerte
    def __init__(self):
        self.context = None
        self.last_error = None

        self.db_name = "Projektarbeit"
        self.address = "localhost"
        self.username = "admin"
        self.password = "admin"


    #Baut die Verbindung mit der Datenbank auf
    def establish_connection(self):
        #Wir haben wieder ein Operation die fehlschlagen könnte, daher brauchen wir wieder einen try except Block
        try:
            #Wenn wir keine Verbindung zur Datenbank haben versuche eine zu öffnen.
            if self.context == None:
                #Versuche eine Verbindung aufzubauen
                self.context = mysql.connector.connect(host=self.address, password=self.password, user=self.username, db=self.db_name, charset="utf8mb4")
                #Hier steht die Verbindung und alle Methoden innerhalb dieser Klasse können sie verwenden.
        #Fehlerbehandlung, wenn wir hier lande konnten wir keine Verbindung aufbauen
        except Error as err:
            # Wenn ein Fehler vorliegt entscheiden wir hier welcher Fehler ausgelöst wurde und setzten last_error auf eine hilfreiche Fehlermeldung.
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.last_error = "Verbindung mit der Datenbank fehlgeschlagen, nutzername oder password falsch."
                print("Verbindung mit der Datenbank fehlgeschlagen, nutzername oder password falsch.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.last_error = f"Die Datenbank '{self.db_name}' existiert nicht."
                print("Die Datenbank 'fuhrpark' existiert nicht.")
            else:
                self.last_error = f"{err}"
                print(err)

    #Diese Methode schließt die Verbindung
    def disconnect(self):
        #Zuerst schließen wir die Verbindung zur Datenbank
        self.context.close()
        #Danach setzten wir die Eigenschaft auf None um interaktion mit einer nicht verbundenen Datenbank zu verhindern.
        self.context = None

    #Fügt neue Daten in die Datenbank ein
    def insert_row(self, query_string, data):
        #Wir testen zuerst ob die Verbindung zur Datenbank vorhanden ist
        if self.context == None:
            #Wenn wir keine Verbindung haben, gebern wir eine Fehlermeldung zurück
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            #Danach kehren wir zum Aufrufer der Methode zurück
            return
        
        #Wenn wir eine Verbindung haben, holen wir uns den cursor der uns vom Mysql Connector zur verfügung gestellt wird.
        cursor = self.context.cursor()

        #Danach testen wir ob der Aufrufer uns Daten gegeben hat die wir in die Datenbank eintragen können
        if data:
            #Jetzt führen wir die Operation aus in dem wir cursor.execute aufrufen mit unserem sql-query (query_string) und den daten die wir
            #eintragen wollen
            cursor.execute(query_string, data)
            #Wir speichern die Id der nächsten Zeile in einer Variable
            mietwagennr = cursor.lastrowid
            #Mit commit() sorgen wir dafür dass die vorherige execute Operation auch wirklich in die Datenbank geschrieben wird.
            context.commit()

    #Rufe alle Daten aus der Datenbank ab
    def query_all_data(self, query_string):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()
    
        #Wir rufen die Daten aus der Datenbank ab, die leeren Klammern geben an dass wir keine Daten für diese Operation übergeben.
        #Immer wenn Klammern ausserhalb eines Methoden oder Funktionenaufrufs erscheinen, haben wir es mit einer Tuple zu tun
        #Eine Tuple kann eine beliebige Anzahl an Werten tragen z.B.:
        #() => Diese Tuple ist leer, sie hat keinen einzigen Wert
        #("hallo",) => Tuple mit einem Eintrag "hallo" das Komma ist nötig da Python sonst nicht weiß wie der Wert zu interpretieren ist.
        #("hallo", 1) => Tuple mit zwei Einträgen "hallo", 1
        #...Eine Tuple hat keine Beschränkung in der Anzahl an Elementen die es beinhalten kann, wichtig ist nur das die Werte durch Komma
        #von einander getrennt sind
        data = cursor.execute(query_string, ())
        #Wir geben die abgerufenen Daten an den Aufrufer zurück
        return cursor

    #Rufe Daten aus der Datenbank ab und Filtere sie.
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

    #Rufe Daten aus der Datenbank ab und filtere sie, ich weiss wirklich nicht warum ich die selbe Funktionalität zweimal implementiert habe,
    #vermutlich müde gewesen :]
    def filter_row(self, query_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()
        cursor.execute(query_string, data)
        return cursor
    
    #Wird verwendet um Zeilen die sich bereits in der Datenbank befinden zu verändern.
    def update_row(self, update_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()

        if data:
            cursor.execute(update_string, data)
            context.commit()

    #Mit dieser Methode lassen sich Zeilen aus der Datenbank löschen
    def delete_row(self, delete_string, data):
        if self.context == None:
            print(f"Fehler keine verbindung zur Datenbank Fehlermeldung: {self.last_error}")
            return

        cursor = self.context.cursor()

        if data:
            cursor.execute(delete_string, data)
            context.commit()
