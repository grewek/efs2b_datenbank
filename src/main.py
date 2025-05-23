import curses
from curses import wrapper
import main_menu
import table_menu
import tui_window

MAIN_MENU_ENTRIES = [
    "a) Eintrag hinzufügen [Hotkey => i]",
    "b) Eintrag ändern     [Hotkey => c]",
    "c) Eintrag löschen    [Hotkey => d]",
    "d) Programm beenden   [Hotkey => q]"
]

def main_basic():
    should_quit = False
    while not should_quit:
        should_quit = main_menu.main_menu()

    print("ALL YOUR DATA ARE BELONG TO US")

def main_curses(stdscr):
    #Funktioniert leider nicht unter Windows...
    screen_width = curses.COLS
    screen_height = curses.LINES
    top_window = int(float(screen_height) * 0.6)    
    bottom_window = int(float(screen_height) * 0.4)
    stdscr.nodelay(True)
    curses.curs_set(0)

    stdscr.clear()

    #START TEST
    # NOTE: This API makes working with the curses window stuff so much simpler :D I should keep this in case i need to work with curses
    # ever again!!
    table_window = tui_window.TuiWindow(screen_width - 1, top_window - 1, 0, 0)

    table_content = table_menu.create_table(table_menu.tabular_data, ["marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"])
    table_window.set_content(table_content.splitlines())

    menu_window = tui_window.TuiWindow(screen_width - 1, bottom_window - 1, 0, top_window)
    menu_window.set_content(MAIN_MENU_ENTRIES)

    #END TEST
     
    while True:
        table_window.update()
        table_window.render(stdscr)

        menu_window.update()
        menu_window.render(stdscr)

        user_input = stdscr.getch()

        if user_input == ord('j'):
            table_window.increment_position()
        elif user_input == ord('k'):
            table_window.decrement_position()
        elif user_input == ord('q'):
            break

if __name__ == "__main__":
    main_basic()
    #wrapper(main)
