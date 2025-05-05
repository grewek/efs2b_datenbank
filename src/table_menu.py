# Format der Daten noch nicht ganz klar, dies ist ein erster Entwurf.
tabular_data = {
    "marke": [ "Audi", "Volkswagen", "BMW", "Opel", "Renault", "Hyundai", "Toyota", ],
    "modell": [ "A3", "Golf", "i3", "Astra", "Clio", "XYZ", "BM-Q" ],
    "farbe": [ "Rot", "Silber", "Grau", "Metallik-Blau", "Schwarz", "Weiß", "Grün"],
    "motorleistung": [120, 220, 330, 440, 80, 90, 55],
    "antriebsart": ["Benziner", "Diesel", "Elektro", "Diesel", "Diesel", "Elektro", "Benziner"],
    "baujahr": [1999, 2000, 2001, 2002, 2003, 2004, 2005],
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

def print_columns(columns, index):
    manufacturers = get_column_from_key(columns, "marke")
    model = get_column_from_key(columns, "modell")
    color = get_column_from_key(columns, "farbe")
    power = get_column_from_key(columns, "motorleistung")
    drive_type = get_column_from_key(columns, "antriebsart")
    manufacture_date = get_column_from_key(columns, "baujahr")
    
    
    longest_entry_manufacturers = find_longest_column(manufacturers, "marke")
    longest_entry_model = find_longest_column(model, "modell")
    longest_entry_color = find_longest_column(color, "farbe")
    longest_entry_power = find_longest_column(power, "motorleistung")
    longest_entry_drive_type = find_longest_column(drive_type, "antriebsart")
    longest_entry_manufacturer_date = find_longest_column(manufacture_date, "baujahr")

    formatted_manufacturer_output = format_column(manufacturers[index], longest_entry_manufacturers)
    formatted_model_output = format_column(model[index], longest_entry_model)
    formatted_color_output = format_column(color[index], longest_entry_color)
    formatted_power_output = format_column(power[index], longest_entry_power)
    formatted_entry_drive_type = format_column(drive_type[index], longest_entry_drive_type)
    formatted_entry_manufacturer_date = format_column(manufacture_date[index], longest_entry_manufacturer_date)

    print(f"{formatted_manufacturer_output}|{formatted_model_output}|{formatted_color_output}|{formatted_power_output}|{formatted_entry_drive_type}|{formatted_entry_manufacturer_date}")

print_columns(tabular_data,1)
#Marke      Modell Farbe   Motorleistung Antriebsart Baujahr Mietpreis
#Volkswagen Golf   Rot     120           Benziner    2012    30
#Audi       A3     Silber  220           Diesel      2018    28
#Toyota     BM-Q   Grau    330           Elektrisch  2024    58
