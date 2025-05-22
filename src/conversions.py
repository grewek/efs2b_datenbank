def get_int(prompt):
    raw_input = input(f"{prompt}:")

    try:
        value = int(raw_input)
        return value
    except ValueError:
        print("Fehler: Eingabe konnte nicht in int konvertiert werden.")

def get_float(prompt):
    raw_input = input(f"{prompt}: ")

    try:
        value = float(raw_input)
        return value
    except ValueError:
        print("Fehler: Eingabe konnte nicht in float konvertiert werden.")


tabular_data = {
    "id": ["Id", 0, 1, 2, 3, 4, 5, 6],
    "marke": [ "Marke", "Audi", "Volkswagen", "BMW", "Opel", "Renault", "Hyundai", "Toyota", ],
    "modell": [ "Modell", "A3", "Golf", "i3", "Astra", "Clio", "XYZ", "BM-Q" ],
    "farbe": [ "Farbe", "Rot", "Silber", "Grau", "Metallik-Blau", "Schwarz", "Weiß", "Grün"],
    "motorleistung": ["Motorleistung", 120, 220, 330, 440, 80, 90, 55],
    "antriebsart": ["Antriebsart", "Benziner", "Diesel", "Elektro", "Diesel", "Diesel", "Elektro", "Benziner"],
    "baujahr": ["Baujahr", 1999, 2000, 2001, 2002, 2003, 2004, 2005],
    "mietpreis": ["Mietpreis", 30, 25, 45, 90, 50, 60, 81]
}
def row_to_column_data(raw_data):
    result = {
        "id": ["ID"],
        "marke": ["Marke"],
        "modell": ["Modell"],
        "farbe": ["Farbe"],
        "motorleistung": ["Motorleistung"],
        "antriebsart": ["Antriebsart"],
        "baujahr": ["Baujahr"],
        "mietpreis": ["Mietpreis"]
    }

    for (id, mark, model, color, power, drive_type, manufacture_date, price) in raw_data:
        result["id"].append(id)
        result["marke"].append(mark)
        result["modell"].append(model)
        result["farbe"].append(color)
        result["motorleistung"].append(power)
        result["antriebsart"].append(drive_type)
        result["baujahr"].append(manufacture_date)
        result["mietpreis"].append(price)
    return result
