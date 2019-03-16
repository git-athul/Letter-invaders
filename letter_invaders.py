"Letter invaders game"

import curses
from time import sleep
from gamelogic import *


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1

def draw(dictionary, window):
    "Draws dictionary in window!"
    height, width = max_dimensions(window)
    for (row, column), letter in dictionary.items():
        if row > height or column > width:
            continue
        window.addch(row, column, letter)

def draw_life(window, letters):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    height, width = max_dimensions(window)
    lifecount = "\u2665 "*life(letters, height)
    init_pos = width - len(lifecount) - 2
    window.addstr(3, init_pos, lifecount, curses.color_pair(1))

def main(window):
    curses.curs_set(0)
    letters = {}
    height, width = max_dimensions(window)
    window.nodelay(True)
    while True:
        window.clear()
        window.border(0)
        letters = new_letter(width, letters)
        letters = move(letters)
        draw(letters, window)
        draw_life(window, letters)
        window.refresh()
        sleep(0.3)
        entry = window.getch()
        if entry != -1:
            letters = kill(letters, chr(entry))
        if life(letters, height) < 0:
            break

if __name__ == '__main__':
    curses.wrapper(main)
