"Letter invaders game"

import curses
from time import sleep
from gamesetup import Setup


def max_dimensions():
    "Dimensions of gamebox"
    height, width = 30, 65
    return height, width

def setup_colors():
    "Setups color_pairs"
    colors = [2, 3, 4, 5, 6, 1, 7]
    # [GREEN, YELLOW, BLUE, MAGENTA, CYAN, RED, WHITE]
    for pos, color in enumerate(colors, start=1):
        curses.init_pair(pos, color, curses.COLOR_BLACK)

def draw(dictionary, window):
    "Draws dictionary in window!"
    height, _ = max_dimensions()

    for (row, column), letter in dictionary.items():
        if row > height:
            continue # Skips these letters
        if letter['char'] == "*":
            window.addstr(row, column, "*", curses.color_pair(6))
            continue
        window.addstr(row, column, letter['char'], curses.color_pair(letter['color']))

def draw_life(dictionary, window):
    "Draws chances left in window"
    height, width = max_dimensions()
    lifecount = "\u2665 "*(CHANCES - Setup(dictionary).life(height))
    init_pos = width - len(lifecount) - 2
    window.addstr(0, init_pos, lifecount, curses.color_pair(6))

def draw_score(window):
    "Draws the score in window"
    string = " Score: {} ".format(SCORE_VALUE)
    window.addstr(0, 2, string, curses.color_pair(7))

def main(window):
    curses.curs_set(0)
    curses.init_color(0, 0, 0, 0) # Black bg
    letters = {}
    height, width = max_dimensions()
    window.nodelay(True)
    setup_colors()

    count = 0
    gap_step = 0
    gap = 7
    switch = True
    req = 7

    global CHANCES
    CHANCES = 7

    global SCORE_VALUE
    SCORE_VALUE = 0
    score = False

    while True:
        screen_h, screen_w = window.getmaxyx()
        if screen_h < height+1 or screen_w < width+1:
            raise SystemExit(
                '''
                Current terminal size: [{0} x {1}]
                Minimum required size: [{2} x {3}]
                '''
                .format(screen_w, screen_h, width+1, height+1))

        window.clear()
        gamebox = window.subwin(height+1, width+1, 0, 0)
        gamebox.box()

        entry = window.getch()
        if entry != -1:
            letters, score = Setup(letters).input_update(chr(entry))
        if Setup(letters).life(height) == CHANCES:
            break

        returns = Setup(letters).letter_generator(width,
                                                  count,
                                                  gap_step, gap,
                                                  switch, req)
        letters, count, gap_step, gap, switch, req = returns
        if score:
            SCORE_VALUE += 8-gap
            score = False
        letters = Setup(letters).move()
        letters = Setup(letters).kill()
        draw(letters, window)
        draw_life(letters, window)
        draw_score(window)
        window.refresh()
        sleep(0.25)

if __name__ == '__main__':
    curses.wrapper(main)
    print("You scored {} points.".format(SCORE_VALUE))
