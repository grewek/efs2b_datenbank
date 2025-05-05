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

#Formatiert und druckt alle spalten in einer Zeile. Code in einem Alptraumhaften zustand, refactor kommt *hoffentlich* morgen!
def print_columns(columns, index):
    #TODO: We need to refactor this mess!
    manufacturers = get_column_from_key(columns, "marke")
    model = get_column_from_key(columns, "modell")
    color = get_column_from_key(columns, "farbe")
    power = get_column_from_key(columns, "motorleistung")
    drive_type = get_column_from_key(columns, "antriebsart")
    manufacture_date = get_column_from_key(columns, "baujahr")
    rent_price = get_column_from_key(columns, "mietpreis")
    
    
    longest_entry_manufacturers = find_longest_column(manufacturers, "marke")
    longest_entry_model = find_longest_column(model, "modell")
    longest_entry_color = find_longest_column(color, "farbe")
    longest_entry_power = find_longest_column(power, "motorleistung")
    longest_entry_drive_type = find_longest_column(drive_type, "antriebsart")
    longest_entry_manufacturer_date = find_longest_column(manufacture_date, "baujahr")
    longest_entry_rent_price = find_longest_column(rent_price, "mietpreis")

    border_manufacturer = "+" + ("-" * (longest_entry_manufacturers)) + "+"
    formatted_manufacturer_output = format_column(manufacturers[index], longest_entry_manufacturers)

    border_model = ("-" * (longest_entry_model)) + "+"
    formatted_model_output = format_column(model[index], longest_entry_model)

    border_color = ("-" * (longest_entry_color)) + "+"
    formatted_color_output = format_column(color[index], longest_entry_color)

    border_power = ("-" * (longest_entry_power)) + "+"
    formatted_power_output = format_column(power[index], longest_entry_power)

    border_drive_type = ("-" * longest_entry_drive_type) + "+"
    formatted_entry_drive_type = format_column(drive_type[index], longest_entry_drive_type)

    border_manufacturer_date = ("-" * longest_entry_manufacturer_date) + "+"
    formatted_entry_manufacturer_date = format_column(manufacture_date[index], longest_entry_manufacturer_date)

    border_rent_price = ("-" * longest_entry_rent_price) + "+"
    formatted_entry_rent_price = format_column(rent_price[index], longest_entry_rent_price)

    if(index == 0):
        print(f"{border_manufacturer}{border_model}{border_color}{border_power}{border_drive_type}{border_manufacturer_date}{border_rent_price}")
        print(f"|{formatted_manufacturer_output}|{formatted_model_output}|{formatted_color_output}|{formatted_power_output}|{formatted_entry_drive_type}|{formatted_entry_manufacturer_date}|{formatted_entry_rent_price}|")
        print(f"{border_manufacturer}{border_model}{border_color}{border_power}{border_drive_type}{border_manufacturer_date}{border_rent_price}")
    else:
        print(f"|{formatted_manufacturer_output}|{formatted_model_output}|{formatted_color_output}|{formatted_power_output}|{formatted_entry_drive_type}|{formatted_entry_manufacturer_date}|{formatted_entry_rent_price}|")
        print(f"{border_manufacturer}{border_model}{border_color}{border_power}{border_drive_type}{border_manufacturer_date}{border_rent_price}")

print_columns(tabular_data,0)
print_columns(tabular_data,1)
print_columns(tabular_data,2)
#Marke      Modell Farbe   Motorleistung Antriebsart Baujahr Mietpreis
#Volkswagen Golf   Rot     120           Benziner    2012    30
#Audi       A3     Silber  220           Diesel      2018    28
#Toyota     BM-Q   Grau    330           Elektrisch  2024    58
