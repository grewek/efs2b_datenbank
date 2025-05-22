import utilities


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
def create_row(columns, column_names, index, closing_border = False):
    #TODO: We need to refactor this mess!
    result = ""
    table_border = ""
    column_content = ""

    for i, column_name in enumerate(column_names):
        column = get_column_from_key(columns, column_name)
        longest_entry = utilities.find_longest_element_in_column(column, column_name)

        if i == 0:
            border = "+" + ("-" * (longest_entry)) + "+"
        else:
            border = ("-" * (longest_entry)) + "+"
        table_border += border;

        formatted_column = format_column(column[index], longest_entry)

        if i == 0:
            column_content += f"|{formatted_column}|"
        else:
            column_content += f"{formatted_column}|"

    result += f"{table_border}\n{column_content}\n"

    if(closing_border):
        result += f"{table_border}"

    return result

def create_table(tabular_data, headers):
    result = ""
    index = 0

    column_length = len(tabular_data[headers[0]])

    for row_index in range(0, column_length):
        if(row_index + 1 == len(headers)):
            result += create_row(tabular_data, headers, row_index, True)
        else:
            result += create_row(tabular_data, headers, row_index)

    return result

