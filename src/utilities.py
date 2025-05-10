#Sucht den längsten Eintrag einer Liste, bei Bedarf kann mit einem minimal Wert
#gestartet werden.
def find_longest_entry_in_list(list, min_length = 0):
    result = min_length

    for entry in list:
        entry_length = len(str(entry))
        if entry_length > result:
            result = entry_length

    return result

#Sucht den längsten Eintrag einer Spalte.
def find_longest_element_in_column(column, default_header):
    minimum_length = len(default_header)
    return find_longest_entry_in_list(column, minimum_length)


def align_line_to_window_center(window_width, largest_entry):
    half_window = int(float(window_width) / 2.0)
    half_element = int(float(largest_entry) / 2.0)

    return half_window - half_element
