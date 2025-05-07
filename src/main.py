import curses
from curses import wrapper
import table_menu


def update(table_view_window):
    table_view_window.addstr(1, 0, "this is a test",)    

def render(stdscr):
    stdscr.refresh()

def main(stdscr):
    screen_width = curses.COLS
    screen_height = curses.LINES
    top_window = int(float(screen_height) * 0.6)    
    bottom_window = int(float(screen_height) * 0.4)
    stdscr.halfdelay(True)

    table_view_window = curses.newwin(top_window, screen_width, 0, 0)
    menu_view_window = curses.newwin(bottom_window, screen_width, top_window, 0)

    stdscr.clear()

    while True:

        table_view_window.refresh()
        update(table_view_window)
        render(stdscr)

        user_input = stdscr.getch()
        if user_input == ord('q'):
            break

if __name__ == "__main__":
    wrapper(main)
