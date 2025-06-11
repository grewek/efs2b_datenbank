import mysql.connector
import table_menu
import conversions
from database import Database
import sql_queries
import datetime

#Die Namen unserer einzelnen Spalten gespeichert als Konstante damit ich sie nicht wieder und wieder tippen muss
HEADERS = ["id", "marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"]

#Konstante Liste mit Namen für mögliche Antriebstypen
POSSIBLE_DRIVE_TYPES = ["Elektro", "Diesel", "Benzin"]
#Konstante Liste mit Namen für mögliche Spalten
POSSIBLE_COLUMNS = ["Marke", "Model", "Farbe", "Leistung", "Antriebsart", "Herstellungsjahr", "Mietpreis"]  
#Konstante Liste mit Name für mögliche Sortierungen
POSSIBLE_SORT_ORDER = ["Aufsteigend", "Absteigend"] 
#Konstante Liste mit den möglichen Optionen für Filter
POSSIBLE_FILTERS = ["Marke", "Antrieb", "Preis"]

#Holt einen Ganzzahligenwert vom Nutzer, wird solange wiederholt bis die Eingabe korrekt ist
def repeated_input_int_value(prompt):
    #Wir wiederholen die Prozedur solange bis der Nutzer eine korrekte Eingabe macht
    while True:
        #Wir rufen die get_int funktion auf und speichern die zurückgegebenen Werte in value und state
        (value, state) = conversions.get_int(f"{prompt}:")

        #Wenn state true ist können wir den Wert value an den Aufrufer zurückgeben
        if state:
            return value
        else:
            #Ansonsten geben wir eine Fehlermeldung aus und wiederholen die Eingabe
            print(f"Der Wert ist ungültig bitte nur Werte eingeben")
#Holt einen Fließkommawert vom Nutzer, wird solange wiederholt bis die Eingabe korrekt ist
def repeated_input_float_value(prompt):
    #Siehe repeated_input_int_value
    while True:
        (value, state) = conversions.get_float(f"{prompt}:")

        if state:
            return value
        else:
            print(f"Der Wert ist ungültig bitte nur Werte eingeben")


#Prüft ob die Eingabe des Nutzer einem der Werte innerhalb der Liste des zweiten Arguments entspricht
def check_validity(user_input, valid_strings):
    #Laufe durch alle optionen die in valid_strings angegeben sind
    for possible_option in valid_strings:
        #Wenn die Nutzereingabe dem Wert possible_options entspricht geben wir true zurück
        if user_input.lower() == possible_option.lower():
            return True

    #Ansonsten geben wir false zurück, wir kennen den eingegebenen Wert nicht
    return False

#Prüft ob ein Wert einem von mehreren möglichen Werten entspricht, wird wiederholt solange dies nicht der Fall ist 
def repeated_input(prompt, possible_values, failure_msg):
    while True:
        #Zeige dem Nutzer die aufforderung zur Eingabe und die mögliche Eingabewerte an
        user_input = input(f"{prompt} {possible_values}: ").lower()
        #Prüfe ob die Eingabe einem der Werte entspricht
        if check_validity(user_input, possible_values):
            #Die eingabe entspricht einem Wert, also geben wir den eingetippten Wert des Nutzers zurück
            return user_input
        else:
            #Fehlschlag wir konnten den Wert nicht verifizieren, wir versuchen es nochmal
            print(f"{failure_msg} {possible_values}")


#Fragt den Nutzer nach den nötigen Daten um eine neue Zeile in die Datenbank einzufügen.
def get_row_data_menu():
    mark = input("Bitte geben sie die Marke des Wagens ein: ")
    model = input("Bitte geben sie den Namen des Modells ein: ")
    color = input("Bitte geben sie die Farbe des Modells ein: ")
    power = repeated_input_int_value("Bitte geben sie die Leistung in PS ein: ")
    #Fragt den Nutzer nach der Antriebsart hier verwenden wir das erste mal repeated input um die Eingabe möglichkeiten
    #des Nutzers zu begrenzen
    drive_type = repeated_input("Bitte geben sie die Antriebsart ein",
                                POSSIBLE_DRIVE_TYPES,
                                "Ungültige eingabe bitte verwenden sie nur die Werte")
    manufacture_date = repeated_input_int_value("Bitte geben sie das Herstellungsjahr ein: ")
    costs_per_day = repeated_input_float_value("Bitte geben sie die täglichen Kosten ein:")

    #Wir geben die Daten als Tuple zurück da der Mysql Connector mit diesen Daten arbeitet
    #außerdem wandeln wir das Jahr mit datetime.date(manufacture_date) in ein gültiges Datum um
    return (mark, model, color, power, drive_type, datetime.date(manufacture_date, 1, 1), costs_per_day)

#Die Funktion wird verwendet um gezielt die Werte einer Zeile zu verändern
def get_updated_data_menu():
    #Zuerst lassen wir den Nutzer spezifizieren welche Zeile er ändern möchte, das passiert über die Eingabe
    #der Mietwagennr
    id = conversions.get_int("Bitte geben sie die ID der zu ändernden Zeile ein: ")
    #Jetzt muss der Nutzer wieder eine Spalte dieser Zeile auswählen die geändert werden soll
    selected_column = repeated_input("Welche Spalte soll geändert werden?",
                                     POSSIBLE_COLUMNS,
                                     "Ungültige eingabe bitte verwenden sie nur die Werte")
    #Dieses if statement prüft welche Spalte wir updaten müssen
    if selected_column == "marke":
        #Wenn wir die Spalte gefunden haben, muss der Nutzer den Namen der neuen Marke eingeben
        mark = input("Bitte geben sie die Bezeichnung der neuen Marke ein:")
        #Danach geben wir den sql_query String zurück und die geänderten Werte
        #Als Rückgabe verwenden wir eine verschachtelte Tuple 
        #Die Zahlen markieren hier die Tuples in Tuple 1 finden wir nur den query und teil 2 beinhaltet nur die Daten
        #die zum updaten der Zeile nötig sind.
        #               1                       2    2
        #               |                       |    |
        return (sql_queries.update_car_mark, (mark, id))
    elif selected_column == "modell":
        model = input("Bitte geben sie die Bezeichnung des Modells ein: ")
        return (sql_queries.update_car_model, (model, id))
    elif selected_column == "farbe":
        color = input("Bitte geben sie die neue Farbe des Fahrzeugs ein: ")
        return (sql_queries.update_car_color, (color, id))
    elif selected_column == "leistung":
        power = repeated_input_int_value("Bitte geben sie die neue Leistung in PS ein: ")
        return (sql_queries.update_car_power, (power, id))
    elif selected_column == "antriebsart":
        drive_type = repeated_input("Bitte geben sie die Antriebsart ein", POSSIBLE_DRIVE_TYPES, "Ungültige eingabe bitte verwenden sie nur die Werte")
        return (sql_queries.update_car_drive_type, (drive_type, id))
    elif selected_column == "herstellungsjahr":
        manufacturer_date = repeated_input_int_value("Bitte geben sie dass Herstellungsjahr ein: ")
        return (sql_queries.update_car_manufacture_date, (date(manufacturer_date, 1, 1), id))
    elif selected_column == "mietpreis":
        costs_per_day = repeated_input_float_value("Bitte geben sie die täglichen Kosten ein:") 
        return (sql_queries.update_car_price, (costs_per_day, id))

def add_row_menu():
    #Ruft get_row_data_menu auf und gibt die Werte zurück
    row_data = get_row_data_menu()
    return row_data

def change_row_menu():
    #Wie oben wir rufen einfach get_updated_data_menu auf und geben die erhaltenen Werte zurück
    update_data = get_updated_data_menu()
    return update_data

#Löscht die Zeile mit der angegebenen ID aus der Datenbank.
def delete_row_menu():
    #Zuerst holen wir die ID der Zeile vom Nutzer
    id = conversions.repeated_input_int_value("Bitte geben sie die ID der zu löschenden Zeile ein: ")
    #Dann geben wir die Werte zurück wie in jedem anderen Fall
    return (sql_queries.delete_car, (id,))

# Ermöglicht die Suche in der Datenbank
def filter_rows_menu():
    to_search = repeated_input(f"Was soll gefiltert werden", POSSIBLE_FILTERS, "Ungültige eingabe bitte verwenden sie nur die Werte")

    if to_search == "marke":
        target_mark = input("Bitte gib den Namen der zu suchenden Marke ein: ")
        return (sql_queries.query_search_mark, (target_mark,))
    elif to_search == "antrieb":
        target_drive_type = repeated_input("Bitte geben sie den gewünschten Antriebstypen an", POSSIBLE_DRIVE_TYPES, "Ungültige eingabe bitte verwenden sie nur die Werte")
        return (sql_queries.query_search_drivetype, (target_drive_type,))
    elif to_search == "preis":
        search_order = repeated_input("Bitte gib an ob der Preis aufsteigend oder absteigend sortiert werden soll", POSSIBLE_SORT_ORDER,
                                      "Ungültige eingabe bitte verwenden sie nur die Werte")
        if search_order == "aufsteigend":
            return (sql_queries.query_search_price_asc, ())
        elif search_order == "absteigend":
            return (sql_queries.query_search_price_desc, ())

# Holt den Mietpreis eines Wagens aus der Datenbank
def calculate_rent_menu():
    id = repeated_input_int_value("ID des gewünschten Fahrzeugs eingeben: ")
    return (sql_queries.query_price, (id,))
    pass

#Das Einstellungsmenü, eingebaut um unterschiedliche Nutzernamen, Passwörter, Datenbanknamen und Remote Hosts zu ermöglichen
def settings_menu(db):
    print(f"a.)Ip Addresse = {db.address}")
    print(f"b.)Nutzername = {db.username}")
    print(f"c.)Passwort = {db.password}")
    print(f"d.)Datenbankname = {db.db_name}")
    print(f"e.)Zurück ins Hauptmenü")
    selection = repeated_input("Ihre Auswahl: ", ["a", "b", "c", "d", "e"],"Ungültige eingabe bitte verwenden sie nur die Werte")

    if selection == "a":
        new_address = input("Bitte geben sie die neue Addresse ein: ")
        #Wir setzten die Eigenschaften der Datenbank auf die neue Werte
        db.address = new_address
    elif selection == "b":
        new_username = input("Bitte geben sie den neuen Nutzernamen ein: ")
        db.username = new_username
    elif selection == "c":
        new_password = input("Bitte geben sie das neue Passwort ein: ")
        db.password = new_password
    elif selection == "d":
        new_db_name = input("Bitte geben sie den neuen Datenbanknamen ein: ")
        db.db_name = new_db_name
    elif selection == "e":
        return
    
#Das Hauptmenü ist verantwortlich für die anzeige des Menüs und verarbeitung von Nutzerinteraktionen
def main_menu(db):
    print("Wilkommen zur Datenbankverwaltung")
    print("================================")
    print("Hauptmenü")
    print("================================")
    print("a.) Datensatz Hinzufügen")
    print("b.) Datensatz ändern")
    print("c.) Datensatz Entfernen")
    print("d.) Alle Mietwagen anzeigen")
    print("e.) Alle Mietwagen filtern")
    print("f.) Mietpreis für Mietwagen berechnen")
    print("g.) Datenbank Einstellungen")
    print("q.) Programm Beenden")
    selection = input("Ihre Auswahl: ")

    if selection == "a":
        #Wir wollen einen Datensatz hinzufügen, also rufen wir add_row_menu auf
        data = add_row_menu()
        #Danach stellen wir sicher, dass wir mit der Datenbank verbunden sind oder bauen eine neue Datenbankverbindung auf
        db.establish_connection()
        #Jetzt rufen wir insert_row aus unserer Datenbanklasse auf und übergeben den query sowie die daten
        db.insert_row(sql_queries.insert_car, data)
    elif selection == "b":
        data = change_row_menu()
        db.establish_connection()
        #Hier holen wir die Daten aus der Tuple, data[0] entspricht dabei dem sql_query und data[1] dem Daten teil z.b. (id, mark)
        db.update_row(data[0], data[1])
    elif selection == "c":
        data = delete_row_menu()
        db.establish_connection()
        db.delete_row(data[0], data[1])
    elif selection == "d":
        db.establish_connection()
        raw_data = db.query_all_data(sql_queries.query_all)
        #Wir stellen sicher, dass wir Daten von der Datenbank erhalten haben
        if raw_data != None:
            #Danach konvertieren wir die erhaltenen Daten in Spaltenform
            table_data = conversions.row_to_column_data(raw_data)
            #Mit diesen konvertierten Daten können wir create_table aufrufen
            table_view = table_menu.create_table(table_data, HEADERS)
            #Die fertige Tabelle stellen wir jetzt auf dem Bildschirm dar
            print(table_view)
        else:
            #Sollte keine Datenbank verbindung zustande kommen, geben wir hier eine Fehlermeldung aus
            print("Operation fehlgeschlagen")
    elif selection == "e":
        user_data = filter_rows_menu()
        filter_query = user_data[0] 
        filter_data = user_data[1]

        db.establish_connection()
        raw_data = db.filter_row(filter_query, filter_data)
        if raw_data != None:
            table_data = conversions.row_to_column_data(raw_data)
            table_view = table_menu.create_table(table_data, HEADERS)
            print(table_view)        
        else:
            print("Operation fehlgeschlagen")
    elif selection == "f":
        user_data = calculate_rent_menu()
        db.establish_connection()
        filter_query = user_data[0]
        filter_data = user_data[1]
        data = db.filter_row(filter_query, filter_data)
        if data != None:
            #Wenn wir die Daten erfolgreich abrufen konnten bitten wir den Nutzer die Mietdauer in Tagen einzugeben
            rent_time = repeated_input_int_value("Bitte geben sie die Mietdauer in Tagen ein: ")
            #Hier erschaffen wir eine neue Variable mit dem Namen preis
            (preis,) = data
            #Hier wird der Preis berechnet
            rent_costs = float(preis[0]) * float(rent_time)
            #Nun erfolgt die Ausgabe auf dem Bildschirm
            print(f"Der Gesamtpreis beträgt: {rent_costs}€")
        else:
            #Keine Verbindung zur Datenbank möglich
            print("Operation fehlgeschlagen")
    elif selection == "g":
        #Wir gehen ins Einstellungsmenü
        settings_menu(db)
    elif selection == "q":
        #Wenn der Nutzer das Program beenden will, geben wir hier True zurück damit sich die Hauptschleife beendet
        return True
    else:
        #Der Nutzer hat eine unbekannte Option benutzt
        print("Unbekannte Option bitte versuche es erneut.")

    input("Bitte eine beliebige Taste drücken um fortzufahren!")
    #Der Nutzer will das Programm nicht beenden wir geben also False zurück damit die Hauptschleife weiterläuft
    return False
