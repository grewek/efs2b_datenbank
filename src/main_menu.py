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

#TODO: Funktionalität ungetestet, sollte laufen aber wenn sich einer die Zeit nimmt und alle optionen einmal durch probiert wäre es besser.
def get_updated_data_menu():
    id = conversions.get_int("Bitte geben sie die ID der zu ändernden Zeile ein: ")
    selected_column = input("Welche Spalte soll geändert werden? (Marke/Model/Farbe/Leistung/Antriebsart/Herstellungsjahr/Mietpreis):")

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
        power = conversions.get_int("Bitte geben sie die neue Leistung in PS ein: ")
        return (sql_queries.update_car_power, (power, id))
    elif selected_column == "antriebsart":
        drive_type = input("Bitte geben sie die Antriebsart ein (Elektro/Diesel/Benzin): ")
        return (sql_queries.update_car_drive_type, (drive_type, id))
    elif selected_column == "herstellungsjahr":
        manufacturer_date = conversions.get_int("Bitte geben sie dass Herstellungsjahr ein: ")
        return (sql_queries.update_car_manufacture_date, (date(manufacturer_date, 1, 1), id))
    elif selected_column == "mietpreis":
        costs_per_day = conversion.get_float("Bitte geben sie die täglichen Kosten ein:") 
        return (sql_queries.update_car_price, (costs_per_day, id))
    else:
        print("Unbekannte Option, kehre ins Hauptmenü zurück")

def add_row_menu():
    id = input("Hier werden die Daten vom Nutzer der Reihe nach abgefragt.")
    row_data = get_row_data_menu()
    return row_data

def change_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    update_data = get_updated_data_menu()
    return update_data

def delete_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Bitte geben sie die ID der zu löschenden Zeile ein: ")

def search_rows_menu():
    input(f"Nach was soll gesucht werden? Mögliche werte {HEADERS}: ")
    search_order = input(f"Soll Aufsteigend oder Absteigend gesucht werden?: ")

def filter_rows_menu():
    to_search = input(f"Was soll gefiltert werden (Marke/Antrieb/Preis): ").lower()

    if to_search == "marke":
        return (sql_queries.query_search_mark, ())
    elif to_search == "antrieb":
        target_drive_type = input("Bitte geben sie den gewünschten Antriebstypen an (Elektro/Diesel/Benziner):")
        return (sql_queries.query_search_drivetype, (target_drive_type,))
    elif to_search == "preis":
        search_order = input("Bitte gib an ob der Preis aufsteigend oder absteigend sortiert werden soll (Aufsteigend/Absteigend): ").lower()
        #TODO: Error Handling
        if search_order == "aufsteigend":
            return (sql_queries.query_search_price_asc, ())
        elif search_order == "absteigend":
            return (sql_queries.query_search_price_desc, ())
    else:
        print(f"Nach dem wert {to_search} kann nicht gefiltert werden.\nKehre ins Hauptmenü zurück.")

def calculate_rent_menu():
    id = input("ID des gewünschten Fahrzeugs eingeben: ")
    rent_length = input("Mietzeitraum in Tagen angeben: ")
    pass

def main_menu():
    print("Wilkommen zur Datenbankverwaltung")
    print("================================")
    print("Hauptmenü")
    print("================================")
    print("a.) Zeile Hinzufügen")
    print("b.) Zeile ändern")
    print("c.) Zeile Entfernen")
    print("d.) Mietwagen anzeigen")
    print("e.) Mietwagen filtern")
    print("f.) Mietpreis berechnen")
    print("q.) Programm Beenden")
    selection = input("Ihre Auswahl: ")

    if selection == "a":
        data = add_row_menu()
        context = database.establish_connection()
        database.insert_row(context, sql_queries.insert_car, data)
    if selection == "b":
        data = change_row_menu()
        context = database.establish_connection()
        database.update_row(context, data[0], data[1])
    if selection == "c":
        delete_row_menu()
    if selection == "d":
        context = database.establish_connection()
        raw_data = database.query_all_data(context, sql_queries.query_all)
        table_data = conversions.row_to_column_data(raw_data)
        table_view = table_menu.create_table(table_data, HEADERS)
        print(table_view)
    if selection == "e":
        user_data = filter_rows_menu()
        filter_query = user_data[0] 
        filter_data = user_data[1]

        context = database.establish_connection()
        raw_data = database.filter_row(context, filter_query, filter_data)
        table_data = conversions.row_to_column_data(raw_data)

        table_view = table_menu.create_table(table_data, HEADERS)
        print(table_view)        
    if selection == "f":
        calculate_rent_menu()
    if selection == "q":
        return True
    else:
        print("Unbekannte Option bitte versuche es erneut.")

    return False
