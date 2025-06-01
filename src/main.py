import main_menu
import table_menu
from database import Database

MAIN_MENU_ENTRIES = [
    "a) Eintrag hinzufügen [Hotkey => i]",
    "b) Eintrag ändern     [Hotkey => c]",
    "c) Eintrag löschen    [Hotkey => d]",
    "d) Programm beenden   [Hotkey => q]"
]

def main_basic():
    should_quit = False
    db = Database()
    while not should_quit:
        should_quit = main_menu.main_menu(db)

    print("Bis bald!")

if __name__ == "__main__":
    main_basic()
