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

get_int("Dies ist ein test")
get_float("Noch ein test")
