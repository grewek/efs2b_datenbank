tabular_data = {
    "row_0": [ ("id", 0), ("marke", "Volkswagen"), ("modell", "Golf"), ("farbe", "Rot"), ("motorleistung", 120), ("antriebsart", "benziner"), ("baujahr", "2012"), ("mietpreis", 30) ]
}

def print_column(column_data, column_length):
    if len(column_data) < column_length:
        rest = (column_length - len(column_data))
        return f"{column_data + ("*" * rest)}"
    else:
        return column_data


print_column("Marke", len("Volkswagen"))
print_column("Volkswagen", len("Volkswagen"))

#Marke      Modell Farbe Motorleistung Antriebsart Baujahr Mietpreis
#Volkswagen Golf   Rot   120           Benziner    2012    30
