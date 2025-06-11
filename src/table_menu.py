import utilities


#Formatiert den Inhalt der Spalten, so dass alle die gleiche Länge haben.
def format_column(column_data, column_length):
    #Sind die Daten der Spalte kleiner als die Maximale Spalten größe?
    if len(str(column_data)) < column_length:
        #Dann berechnen wir viele Zeichen uns bis zum maximum fehlen
        rest = (column_length - len(str(column_data)))
        #Und erweitern es mit Leerzeichen um die Strings auf die gleiche Länge zu bringen.
        content = str(column_data) + (" " * rest)
        #Wir geben das ergebnis als formatierten string zurück
        return f"{content}"
    else:
        return column_data

#Gibt die Werte der angeforderten Spalte zurück.
def get_column_from_key(column_data, key):
    return column_data[key]

#Generiert eine Spalte
def create_row(columns, column_names, index, closing_border = False):
    #Result speichert das gesamte ergebnis
    result = ""
    #table_border beinhaltet die Linien zwischen den Table
    table_border = ""
    column_content = ""

    for i, column_name in enumerate(column_names):
        #Hole die Daten der Spalte mit dem angegebenen Namen
        column = get_column_from_key(columns, column_name)
        #Wir suchen den längsten Eintrag dieser Spalte
        longest_entry = utilities.find_longest_element_in_column(column, column_name)

        #Erste Spalte? Wir müssen ein weiteres + hinzufügen um den Rand zu vervollständigen AUSGABE: "+----------+"
        if i == 0:
            border = "+" + ("-" * (longest_entry)) + "+"
        else:
            #Ansonsten generieren wir den "Rand" für diese Spalte AUSGABE: "-----------+"
            border = ("-" * (longest_entry)) + "+"
        #Wir hängen alle Teile die wir generieren an den schon generierten table_border an
        table_border += border;

        #Bringt den eigentlichen Inhalt der Spalte auf eine gemeinsame länge
        formatted_column = format_column(column[index], longest_entry)

        #Wieder ein Edgecase, wenn wir am Anfang der Zeile sind brauchen wir zwei || anstatt einem AUSGABE: "|hallo efs2b|"
        if i == 0:
            column_content += f"|{formatted_column}|"
        else:
            #Ansonsten begnügen wir uns mit einer AUSGABE: "hallo efs2b|"
            column_content += f"{formatted_column}|"

    #Jetzt fügen wir den Inhalt und die Ränder in einem String zusammen
    result += f"{table_border}\n{column_content}\n"

    #Wenn der Nutzer möchte können wir noch einen abschließenden Rand einfügen
    if(closing_border):
        result += f"{table_border}"

    #Dann geben wir das Ergebnis zurück 
    return result

def create_table(tabular_data, headers):
    result = ""
    index = 0

    #Holt die Anzahl an Einträgen pro Spalte
    column_length = len(tabular_data[headers[0]])

    for row_index in range(0, column_length):
        if(row_index + 1 == len(headers)):
            result += create_row(tabular_data, headers, row_index, True)
        else:
            result += create_row(tabular_data, headers, row_index)

    return result

