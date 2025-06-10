#Fordert den Nutzer auf einen Ganzzahligenwert einzugeben
def get_int(prompt):
    # Zeigt die Prompt an, die an die Funktion übergeben wurde.
    #Nach der prompt kann der Nutzer eine Zahl angeben.
    raw_input = input(f"{prompt}:")

    #Das umwandeln eines Wertes kann fehlschlagen daher benötigen wir hier einen try except block
    #um mögliche Ausnahmen abzufangen
    try:
        #Versuche den Wert in eine Ganzzahl zu konvertieren
        value = int(raw_input)
        #Wenn die Konvertierung geklappt hat geben wir den vom Nutzer eingetippten Wert und einen boolschen Wert zurück
        #Der Boolsche Wert ist true da die Umwandlung erfolgreich verlief
        return (value, True)
    except ValueError:
        #Die Konvertierung hat nicht geklappt, also signalisieren wir durch den Wert None das die Eingabe vom Nutzer ungültig war
        #zudem geben wir ebenfalls False damit wir sicher wissen dass die Operation fehlschlug
        return (None, False)

#Fordert den Nutzer auf einen Fließkommawert einzugeben
def get_float(prompt):
    #Zeigt den Prompt an siehe die get_int Funktion
    raw_input = input(f"{prompt}: ")

    #Funktioniert genau wie die get_int Funktion nur dass die Funktion nach float() konvertiert und nicht nach int()
    try:
        value = float(raw_input)
        return (value, True)
    except ValueError:
        return (None, False)

#Wandelt die Daten die aus der Datenbank ausgelsen wurden in ein Spaltenformat um
def row_to_column_data(raw_data):
    #Da die Daten von der Schnittstelle der Datenbank in einem Zeileformat kommen müssen wir sie
    #erst in ein Spaltenformat umwandeln, das passiert hier.
    #Zuerst erstellen wir ein Dictionary das alle Spalten beinhaltet mit denen wir Arbeiten. Jede Spalte
    #beinhaltet eine Liste mit den Element die sich in der Spalte befinden das erste Element ist immer
    #der Name der Spalte. 
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

    #Jetzt durchlaufen wir alle Zeilen die uns von der Datenbank übergeben wurden und sortieren sie ein
    for (id, mark, model, color, power, drive_type, manufacture_date, price) in raw_data:
        #Für jede Zeile legen wir einen neuen Eintrag in unseren Spaltenlisten an
        result["id"].append(id)
        result["marke"].append(mark)
        result["modell"].append(model)
        result["farbe"].append(color)
        result["motorleistung"].append(power)
        result["antriebsart"].append(drive_type)
        result["baujahr"].append(manufacture_date)
        result["mietpreis"].append(price)

    #Wenn wir alle Zeilen verarbeitet haben, geben wir unser mit Daten gefülltes Dictionary zurück
    return result
