# Format der Daten noch nicht ganz klar, dies ist ein erster Entwurf.
tabular_data = {
    "marke": [ "Marke", "Audi", "Volkswagen", "BMW", "Opel", "Renault", "Hyundai", "Toyota", ],
    "modell": [ "Modell", "A3", "Golf", "i3", "Astra", "Clio", "XYZ", "BM-Q" ],
    "farbe": [ "Farbe", "Rot", "Silber", "Grau", "Metallik-Blau", "Schwarz", "Weiß", "Grün"],
    "motorleistung": ["Motorleistung", 120, 220, 330, 440, 80, 90, 55],
    "antriebsart": ["Antriebsart", "Benziner", "Diesel", "Elektro", "Diesel", "Diesel", "Elektro", "Benziner"],
    "baujahr": ["Baujahr", 1999, 2000, 2001, 2002, 2003, 2004, 2005],
    "mietpreis": ["Mietpreis", 30, 25, 45, 90, 50, 60, 81]
}

#Findet die längste Zeile einer Spalte.
def find_longest_column(columns, default_header):
    result = len(default_header)
    for column in columns:
        if len(str(column)) > result:
            result = len(str(column))

    return result

#Formatiert den Inhalt der Spalten, so dass alle die gleiche Länge haben.
def format_column(column_data, column_length):
    if len(str(column_data)) < column_length:
        rest = (column_length - len(str(column_data)))
        return f"{str(column_data) + (" " * rest)}"
    else:
        return column_data

#Gibt die Werte der angeforderten Spalte zurück.
def get_column_from_key(column_data, key):
    return column_data[key]

#TODO: Wir sollten die generierung des Randes in eine eigene Funktion auslagern.
def print_columns(columns, column_names, index):
    #TODO: We need to refactor this mess!
    result_border = ""
    result = ""
    for i, column_name in enumerate(column_names):
        column = get_column_from_key(columns, column_name)
        longest_entry = find_longest_column(column, column_name)

        if i == 0:
            border = "+" + ("-" * (longest_entry)) + "+"
        else:
            border = ("-" * (longest_entry)) + "+"
        result_border += border;

        formatted_column = format_column(column[index], longest_entry)

        if i == 0:
            result += f"|{formatted_column}|"
        else:
            result += f"{formatted_column}|"

    print(result_border)
    print(result)

print_columns(tabular_data,["marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"],0)
print_columns(tabular_data,["marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"],1)
print_columns(tabular_data,["marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"],2)
#Marke      Modell Farbe   Motorleistung Antriebsart Baujahr Mietpreis
#Volkswagen Golf   Rot     120           Benziner    2012    30
#Audi       A3     Silber  220           Diesel      2018    28
#Toyota     BM-Q   Grau    330           Elektrisch  2024    58
