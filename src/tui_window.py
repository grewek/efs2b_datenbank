import utilities
import curses

class TuiWindow:
    def __init__(self, width, height, start_x, start_y):
        self.raw_content = []

        self.width = width
        self.height = height
        self.start_y = start_y
        self.start_x = start_x

        self.center_x = 0
        self.position = 0

        self.longest_entry = 0
        self.align_center = True
        self.window = curses.newwin(self.height, self.width, self.start_y, self.start_x);

    def increment_position(self):
        if self.position < len(self.raw_content):
            self.position += 1

    def decrement_position(self):
        if self.position > 0:
            self.position -= 1
        
    def set_content(self, content):
        self.raw_content = content

    def update(self):
        if self.align_center:
            #TODO: We don't need to find the longest entry every time we update, we can cache the result!
            self.longest_entry = utilities.find_longest_entry_in_list(self.raw_content)
            self.center_x = utilities.align_line_to_window_center(self.width, self.longest_entry)

        start_slice_position = self.position
        end_slice_position = self.position + self.height - 1
        
        content_to_render = self.raw_content[start_slice_position:end_slice_position]

        for i, line in enumerate(content_to_render):
            if self.align_center:
                self.window.addstr(i, self.center_x, line)
            else:
                self.window.addstr(i, 0, line)

    def render(self, stdscr):
        self.window.refresh()
