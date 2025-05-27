import mysql.connector
import table_menu
import conversions
from database import Database
import sql_queries
import datetime

HEADERS = ["id", "marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"]

POSSIBLE_DRIVE_TYPES = ["Elektro", "Diesel", "Benzin"]
POSSIBLE_COLUMNS = ["Marke", "Model", "Farbe", "Leistung", "Antriebsart", "Herstellungsjahr", "Mietpreis"]  
POSSIBLE_SORT_ORDER = ["Aufsteigend", "Absteigend"] 
POSSIBLE_FILTERS = ["Marke", "Antrieb", "Preis"]

def repeated_input_int_value(prompt):
    while True:
        (value, state) = conversions.get_int(f"{prompt}:")

        if state:
            return value
        else:
            print(f"Der Wert ist ungültig bitte nur Werte eingeben")

def repeated_input_float_value(prompt):
    while True:
        (value, state) = conversions.get_float(f"{prompt}:")

        if state:
            return value
        else:
            print(f"Der Wert ist ungültig bitte nur Werte eingeben")


def check_validity(user_input, valid_strings):
    for possible_option in valid_strings:
        if user_input.lower() == possible_option.lower():
            return True

    return False

def repeated_input(prompt, possible_values, failure_msg):
    while True:
        user_input = input(f"{prompt} {possible_values}: ").lower()
        if check_validity(user_input, possible_values):
            return user_input
        else:
            print(f"{failure_msg} {possible_values}")

def get_row_data_menu():
    mark = input("Bitte geben sie die Marke des Wagens ein: ")
    model = input("Bitte geben sie den Namen des Modells ein: ")
    color = input("Bitte geben sie die Farbe des Modells ein: ")
    power = repeated_input_int_value("Bitte geben sie die Leistung in PS ein: ")
    drive_type = repeated_input("Bitte geben sie die Antriebsart ein",
                                POSSIBLE_DRIVE_TYPES,
                                "Ungültige eingabe bitte verwenden sie nur die Werte")
    manufacture_date = repeated_input_int_value("Bitte geben sie das Herstellungsjahr ein: ")
    costs_per_day = repeated_input_float_value("Bitte geben sie die täglichen Kosten ein:")

    return (mark, model, color, power, drive_type, datetime.date(manufacture_date, 1, 1), costs_per_day)

#TODO: Funktionalität ungetestet, sollte laufen aber wenn sich einer die Zeit nimmt und alle optionen einmal durch probiert wäre es besser.
def get_updated_data_menu():
    id = conversions.get_int("Bitte geben sie die ID der zu ändernden Zeile ein: ")
    selected_column = repeated_input("Welche Spalte soll geändert werden?",
                                     POSSIBLE_COLUMNS,
                                     "Ungültige eingabe bitte verwenden sie nur die Werte")
    if selected_column == "marke":
        mark = input("Bitte geben sie die Bezeichnung der neuen Marke ein:")
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
    row_data = get_row_data_menu()
    return row_data

def change_row_menu():
    update_data = get_updated_data_menu()
    return update_data

def delete_row_menu():
    id = conversions.repeated_input_int_value("Bitte geben sie die ID der zu löschenden Zeile ein: ")
    return (sql_queries.delete_car, (id,))


def search_rows_menu():
    input(f"Nach was soll gesucht werden? Mögliche werte ({HEADERS}): ")
    search_order = repeated_input(f"Soll Aufsteigend oder Absteigend gesucht werden?", POSSIBLE_SORT_ORDER, "Ungültige eingabe bitte verwenden sie nur die Werte")

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

def calculate_rent_menu():
    id = repeated_input_int_value("ID des gewünschten Fahrzeugs eingeben: ")
    return (sql_queries.query_price, (id,))
    pass

def settings_menu(db):
    print(f"a.)Ip Addresse = {db.get_address()}")
    print(f"b.)Nutzername = {db.get_username()}")
    print(f"c.)Passwort = {db.get_password()}")
    print(f"d.)Datenbankname = {db.get_name()}")
    print(f"e.)Zurück ins Hauptmenü")
    selection = repeated_input("Ihre Auswahl: ", ["a", "b", "c", "d", "e"],"Ungültige eingabe bitte verwenden sie nur die Werte")

    if selection == "a":
        new_address = input("Bitte geben sie die neue Addresse ein: ")
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
        data = add_row_menu()
        db.establish_connection()
        db.insert_row(sql_queries.insert_car, data)
    elif selection == "b":
        data = change_row_menu()
        db.establish_connection()
        db.update_row(data[0], data[1])
    elif selection == "c":
        data = delete_row_menu()
        db.establish_connection()
        db.delete_row(data[0], data[1])
    elif selection == "d":
        db.establish_connection()
        raw_data = db.query_all_data(sql_queries.query_all)
        if raw_data != None:
            table_data = conversions.row_to_column_data(raw_data)
            table_view = table_menu.create_table(table_data, HEADERS)
            print(table_view)
        else:
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
            rent_time = repeated_input_int_value("Bitte geben sie die Mietdauer in Tagen ein: ")
            (preis,) = data
            rent_costs = float(preis[0]) * float(rent_time)
            print(f"Der Gesamtpreis beträgt: {rent_costs}€")
        else:
            print("Operation fehlgeschlagen")
    elif selection == "g":
        settings_menu(db)
    elif selection == "q":
        return True
    else:
        print("Unbekannte Option bitte versuche es erneut.")

    input("Bitte eine beliebige Taste drücken um fortzufahren!")
    return False
