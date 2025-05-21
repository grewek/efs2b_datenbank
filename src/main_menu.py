import mysql.connector
import table_menu
import conversions
import database
import sql_queries
import datetime

HEADERS = ["id", "marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"]

def get_row_data_menu():
    mark = input("Bitte geben sie die Marke des Wagens ein: ")
    model = input("Bitte geben sie den Namen des Modells ein: ")
    color = input("Bitte geben sie die Farbe des Modells ein: ")
    power = conversions.get_int("Bitte geben sie die Leistung in PS ein: ")
    drive_type = input("Bitte geben sie die Antriebsart ein (Elektro/Diesel/Benzin): ")
    manufacture_date = conversions.get_int("Bitte geben sie das Herstellungsjahr ein: ")
    costs_per_day = conversions.get_float("Bitte geben sie die täglichen Kosten ein:")

    return (mark, model, color, power, drive_type, datetime.date(manufacture_date, 1, 1), costs_per_day)

def add_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Hier werden die Daten vom Nutzer der Reihe nach abgefragt.")
    row_data = get_row_data_menu()
    return row_data

def change_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Bitte geben sie die ID der zu ändernden Zeile ein: ")

def delete_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Bitte geben sie die ID der zu löschenden Zeile ein: ")

def search_rows_menu():
    input(f"Nach was soll gesucht werden? Mögliche werte {HEADERS}: ")
    search_order = input(f"Soll Aufsteigend oder Absteigend gesucht werden?: ")

def calculate_rent_menu():
    id = input("ID des gewünschten Fahrzeugs eingeben: ")
    rent_length = input("Mietzeitraum in Tagen angeben: ")
    pass

def filter_rows_menu():
    pass

def main_menu():
    print("Wilkommen zur Datenbankverwaltung")
    print("================================")
    print("Hauptmenü")
    print("================================")
    print("a.) Zeile Hinzufügen")
    print("b.) Zeile ändern")
    print("c.) Zeile Entfernen")
    print("d.) Datensatz durchsuchen")
    print("e.) Datensatz Filtern")
    print("f.) Mietpreis berechnen")
    print("g.) Programm Beenden")
    selection = input("Ihre Auswahl: ")

    if selection == "a":
        data = add_row_menu()
        context = database.establish_connection()
        database.insert_row(context, sql_queries.insert_car, data)
    if selection == "b":
        change_row_menu()
    if selection == "c":
        delete_row_menu()
    if selection == "d":
        search_rows_menu()
    if selection == "e":
        filter_rows_menu()
    if selection == "f":
        calculate_rent_menu()
    else:
        print("Unbekannte Option bitte versuche es erneut.")

    return False
