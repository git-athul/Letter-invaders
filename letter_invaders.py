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

def main(window):
    curses.curs_set(0)
    letters = {}
    height, width = max_dimensions(window)
    window.nodelay(True)
    while True:
        window.clear()
        window.border(0)
        if life(letters, height) < 0:
            break
        letters = new_letter(width, letters)
        letters = move(letters)
        draw(letters, window)
        window.refresh()
        sleep(0.3)
        entry = window.getch()
        if entry != -1:
            letters = kill(letters, chr(entry))

if __name__ == '__main__':
    curses.wrapper(main)
