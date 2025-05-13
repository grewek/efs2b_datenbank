import table_menu

HEADERS = ["id", "marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"]

def add_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Hier werden die Daten vom Nutzer der Reihe nach abgefragt.")

def change_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Bitte gib die ID der zu ändernden Zeile ein: ")

def delete_row_menu():
    table_view = table_menu.create_table(table_menu.tabular_data, HEADERS)
    print(table_view)
    id = input("Bitte gib die ID der zu löschenden Zeile ein: ")

def search_rows_menu():
    input(f"Nach was soll gesucht werden? Mögliche werte {HEADERS}: ")
    search_order = input(f"Soll Aufsteigend oder Absteigend gesucht werden?: ")

def calculate_rent_menu():
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
        add_row_menu()
    if selection == "b":
        change_row_menu()
    if selection == "c":
        delete_row_menu()
    if selection == "d":
        search_rows_menu()
    if selection == "e":
        filter_rows_menu()
    if selection == "f"
        calculate_rent_menu()
    else:
        print("Unbekannte Option bitte versuche es erneut.")

    return False
