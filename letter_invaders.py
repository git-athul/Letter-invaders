"Letter invaders game"

import curses
from time import sleep
from gamesetup import Setup


HEIGHT, WIDTH = 30, 65
CHANCES = 7
SCORE_VALUE = 0


def check_window(window):
    "Checks the dimensions of terminal"
    screen_h, screen_w = window.getmaxyx()
    if screen_h < HEIGHT+1 or screen_w < WIDTH+1:
        raise SystemExit(
            '''
            Current terminal size: [{0} x {1}]
            Minimum required size: [{2} x {3}]
            '''
            .format(screen_w, screen_h, WIDTH+1, HEIGHT+1))


def setup_colors():
    "Setups color_pairs"
    colors = [2, 3, 4, 5, 6, 1, 7]
    # [GREEN, YELLOW, BLUE, MAGENTA, CYAN, RED, WHITE]
    for pos, color in enumerate(colors, start=1):
        curses.init_pair(pos, color, curses.COLOR_BLACK)

def draw(dictionary, window):
    "Draws dictionary in window!"
    for (row, column), letter in dictionary.items():
        if row > HEIGHT:
            continue # Skips these letters
        if letter['char'] == "*":
            window.addstr(row, column, "*", curses.color_pair(6))
            continue
        window.addstr(row, column, letter['char'], curses.color_pair(letter['color']))

def draw_life(lifecount, window):
    "Draws chances left in window"
    lifecount = "\u2665 "*(CHANCES - lifecount)
    init_pos = WIDTH - len(lifecount) - 2
    window.addstr(0, init_pos, lifecount, curses.color_pair(6))

def draw_score(window):
    "Draws the score in window"
    string = " Score: {} ".format(SCORE_VALUE)
    window.addstr(0, 2, string, curses.color_pair(7))

def main(window):
    curses.curs_set(0)
    curses.init_color(0, 0, 0, 0) # Black bg
    setup_colors()
    window.nodelay(True)
    letters = {}

    settings = {'letter_count':0,
                'switch':True,
                'gap_step':0,
                'gap':7,
                'level_req':7}
    global SCORE_VALUE
    lifecount = 0

    while True:
        check_window(window)
        window.clear()
        gamebox = window.subwin(HEIGHT+1, WIDTH+1, 0, 0)
        gamebox.box()

        entry = window.getch()
        if entry != -1:
            letters, score = Setup(letters).input_update(chr(entry))
            if score:
                SCORE_VALUE += 8 - settings['gap']
        if lifecount == CHANCES:
            break

        letters, settings = Setup(letters).letter_generator(WIDTH, settings)
        letters = Setup(letters).move()
        letters = Setup(letters).kill()
        lifecount = Setup(letters).life(HEIGHT, lifecount)
        draw(letters, window)
        draw_life(lifecount, window)
        draw_score(window)
        window.refresh()
        sleep(0.25)

if __name__ == '__main__':
    curses.wrapper(main)
    print("You scored {} points.".format(SCORE_VALUE))
