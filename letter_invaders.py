"Letter invaders game"

import curses
from time import sleep
from gamesetup import Setup


def max_dimensions():
    "Dimensions of "
    height, width = 30, 65
    return height, width

def draw(dictionary, window):
    "Draws dictionary in window!"
    height, width = max_dimensions()
    colors = [2, 3, 4, 5, 6]
    # [curses.COLOR_GREEN,
    #      curses.COLOR_YELLOW,
    #      curses.COLOR_BLUE,
    #      curses.COLOR_MAGENTA,
    #      curses.COLOR_CYAN]
    for pos, color in enumerate(colors, start=3):
        curses.init_pair(pos, color, curses.COLOR_BLACK)

    for (row, column), letter in dictionary.items():
        if row > height or column > width:
            continue
        window.addstr(row, column, letter['char'], curses.color_pair(letter['color']))

def draw_life(window, letters):
    "Draws chances in window"
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    height, width = max_dimensions()
    lifecount = "\u2665 "*(7-Setup(letters).life(height))
    init_pos = width - len(lifecount) - 2
    window.addstr(0, init_pos, lifecount, curses.color_pair(1))

def main(window):
    curses.curs_set(0)
    letters = {}
    height, width = max_dimensions()
    window.nodelay(True)

    count = 0
    gap_step = 0
    gap = 7
    switch = True
    req = 7

    while True:
        screen_h, screen_w = window.getmaxyx()
        if screen_h < height or screen_w < width:
            raise SystemExit(
                '''Current terminal size: [{0} x {1}]
Minimum required size: [{2} x {3}]'''
                .format(screen_w, screen_h, width, height))

        window.clear()
        gamebox = window.subwin(height+1, width+1, 0, 0)
        gamebox.box()

        returns = Setup(letters).letter_generator(width,
                                                  count,
                                                  gap_step, gap,
                                                  switch, req)
        letters, count, gap_step, gap, switch, req = returns

        letters = Setup(letters).move()
        draw(letters, window)
        draw_life(window, letters)
        window.refresh()
        entry = window.getch()
        if entry != -1:
            letters = Setup(letters).kill(chr(entry))
        if Setup(letters).life(height) == 7:
            break
        sleep(0.25)

if __name__ == '__main__':
    curses.wrapper(main)
