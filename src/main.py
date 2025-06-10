import main_menu
import table_menu
from database import Database

#Hier startet das eigentliche Programm
def main_basic():
    #Variable die angibt ob sich das Programm beenden sollte oder nicht
    should_quit = False
    #Wir konstruieren ein neues Objekt aus der Datenbank klasse und speichern es in einer Variable
    db = Database()
    #Solange should_quit nicht true ist sollte das Programm weiterlaufen
    while not should_quit:
        #Wir rufen die main_menu Funktion auf, der Aufruf gibt uns als Rückgabewert true oder false zurück
        #wenn der Wert true ist, beenden wir das Programm
        should_quit = main_menu.main_menu(db)

    #Einen letzten Gruß an den Nutzer.
    print("Bis bald!")

#If statement das prüft, ob diese Datei mit dem python3 interpreter gestartet wurde.
if __name__ == "__main__":
    main_basic()
