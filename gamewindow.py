import curses

class Window():
    "Functions to display letter-invaders-game"

    def __init__(self, screen, height, width):
        self.win = screen
        self.height = height
        self.width = width
        self.score_value = 0
        Window.setup_colors()
        self.win.nodelay(True)
        curses.init_color(curses.COLOR_BLACK, 0, 0, 0) # Black BG
        curses.curs_set(0)


    def make_subwindow(self):
        "Checks the dimensions of terminal and makes subwindow"
        self.win.clear()
        screen_h, screen_w = self.win.getmaxyx()
        if screen_h < self.height+1 or screen_w < self.width+1:
            raise SystemExit(
                '''Current terminal size: [{0} x {1}]
Minimum required size: [{2} x {3}]'''
                .format(screen_w, screen_h, self.width+1, self.height+1))
        gamebox = self.win.subwin(self.height+1, self.width+1, 0, 0)
        gamebox.box()

    def take_input(self, dictionary, settings):
        "Takes input, updates dictionary and calculates score"
        entry = self.win.getch()
        if entry != -1:
            _, score = dictionary.update_input(chr(entry))
            if score:
                self.score_value += 8 - settings['gap']

    def setup_colors():
        "Setups color_pairs"
        colors = [2, 3, 4, 5, 6, 1, 7]
        # [GREEN, YELLOW, BLUE, MAGENTA, CYAN, RED, WHITE]
        for pos, color in enumerate(colors, start=1):
            curses.init_pair(pos, color, curses.COLOR_BLACK)

    def draw_life(self, lifecount, chances):
        "Draws chances left in window"
        count = "\u2665 "*(chances - lifecount)
        pos = self.width - len(count) - 2
        self.win.addstr(0, pos, count, curses.color_pair(6)) # RED

    def draw_score(self):
        "Draws the score in window"
        string = " Score: {} ".format(self.score_value)
        self.win.addstr(0, 2, string, curses.color_pair(7)) # WHITE

    def draw(self, dictionary, lifecount, chances):
        "Draws game in window!"
        for (row, column), letter in dictionary.items():
            self.win.addstr(row, column, letter['char'],
                            curses.color_pair(letter['color']))
        Window.draw_life(self, lifecount, chances)
        Window.draw_score(self)
        self.win.refresh()

    def finalscore(self):
        "returns finalscore"
        return self.score_value
