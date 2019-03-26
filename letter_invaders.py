"Letter invaders game"

import curses
from time import sleep
from gamesetup import Setup


HEIGHT, WIDTH = 30, 65
CHANCES = 7
SCORE_VALUE = 0


def make_subwindow(window):
    "Checks the dimensions of terminal and makes subwindow"
    window.clear()
    screen_h, screen_w = window.getmaxyx()
    if screen_h < HEIGHT+1 or screen_w < WIDTH+1:
        raise SystemExit(
            '''Current terminal size: [{0} x {1}]
Minimum required size: [{2} x {3}]'''
            .format(screen_w, screen_h, WIDTH+1, HEIGHT+1))
    gamebox = window.subwin(HEIGHT+1, WIDTH+1, 0, 0)
    gamebox.box()

def take_input(dictionary, settings, window):
    "Takes input, updates dictionary and calculates score"
    global SCORE_VALUE
    entry = window.getch()
    if entry != -1:
        _, score = dictionary.update_input(chr(entry))
        if score:
            SCORE_VALUE += 8 - settings['gap']

def setup_colors():
    "Setups color_pairs"
    colors = [2, 3, 4, 5, 6, 1, 7]
    # [GREEN, YELLOW, BLUE, MAGENTA, CYAN, RED, WHITE]
    for pos, color in enumerate(colors, start=1):
        curses.init_pair(pos, color, curses.COLOR_BLACK)

def draw_life(lifecount, window):
    "Draws chances left in window"
    count = "\u2665 "*(CHANCES - lifecount)
    init_pos = WIDTH - len(count) - 2
    window.addstr(0, init_pos, count, curses.color_pair(6)) # RED

def draw_score(window):
    "Draws the score in window"
    string = " Score: {} ".format(SCORE_VALUE)
    window.addstr(0, 2, string, curses.color_pair(7)) # WHITE

def draw(dictionary, lifecount, window):
    "Draws game in window!"
    for (row, column), letter in dictionary.items():
        window.addstr(row, column, letter['char'],
                      curses.color_pair(letter['color']))
    draw_life(lifecount, window)
    draw_score(window)


def main(window):
    window.nodelay(True)
    curses.init_color(curses.COLOR_BLACK, 0, 0, 0) # Black background
    curses.curs_set(0)
    setup_colors()

    settings = {'letter_count':0, 'switch':True,
                'gap_step':0, 'gap':7, 'level_req':7}
    lifecount = 0
    letters = {}

    while True:
        make_subwindow(window)
        letters = Setup(letters)
        take_input(letters, settings, window)
        _, settings = letters.generate_letter(WIDTH, settings)
        letters.move()
        lifecount = letters.count_life(HEIGHT, lifecount)
        letters = letters.expire_entered()
        if lifecount == CHANCES:
            break
        draw(letters, lifecount, window)
        window.refresh()
        sleep(0.25)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
        print("You scored {} points.".format(SCORE_VALUE))
    except KeyboardInterrupt:
        print("Interrupted!")
