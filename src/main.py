import curses
from curses import wrapper
import table_menu
import utilities

MAIN_MENU_ENTRIES = [
    "a) Eintrag hinzufügen [Hotkey => i]",
    "b) Eintrag ändern     [Hotkey => c]",
    "c) Eintrag löschen    [Hotkey => d]",
    "d) Programm beenden   [Hotkey => q]"
]

def update(stdscr, table_view_window, menu_view_window):
    update_table_view_window(table_view_window)
    update_menu_view_window(menu_view_window)

def update_menu_view_window(menu_view_window):
        longest_menu_entry = utilities.find_longest_entry_in_list(MAIN_MENU_ENTRIES)
        center_x = utilities.align_line_to_window_center(curses.COLS, longest_menu_entry)

        for i, entry in enumerate(MAIN_MENU_ENTRIES):
            menu_view_window.addstr(i,center_x, entry)

def update_table_view_window(table_view_window):
    table = table_menu.create_table(table_menu.tabular_data, ["marke", "modell", "farbe", "motorleistung", "antriebsart", "baujahr", "mietpreis"])

    table_lines = table.splitlines()

    #TODO: Line needs to be refactored to be more readable...
    #TODO: Use the new utility function!
    x_align_center= int(float(curses.COLS) / 2.0) - int((float(len(table_lines[0])) / 2.0))

    for i, line in enumerate(table_lines):
        table_view_window.addstr(i, x_align_center, line)    

def render(stdscr, table_view_window, menu_view_window):
    render_table_view(table_view_window)
    render_menu_view(menu_view_window)
    stdscr.refresh()

def render_table_view(table_view_window):
    table_view_window.refresh()

def render_menu_view(menu_view_window):
    menu_view_window.refresh()

def main(stdscr):
    screen_width = curses.COLS
    screen_height = curses.LINES
    top_window = int(float(screen_height) * 0.6)    
    bottom_window = int(float(screen_height) * 0.4)
    stdscr.nodelay(True)
    curses.curs_set(0)

    table_view_window = curses.newwin(top_window - 1, screen_width - 1, 0, 0)
    menu_view_window = curses.newwin(bottom_window - 1, screen_width - 1, top_window, 0)

    stdscr.clear()

    while True:
        table_view_window.refresh()
        update(stdscr, table_view_window, menu_view_window)
        render(stdscr, table_view_window, menu_view_window)

        user_input = stdscr.getch()
        if user_input == ord('q'):
            break

if __name__ == "__main__":
    wrapper(main)
