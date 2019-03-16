"Letter invaders game"

import curses
from time import sleep
from gamelogic import *

def draw(dictionary, window):
    "Draws dictionary in window!"
    for (row, column), letter in dictionary.items():
        window.addch(row, column, letter)

def main(window):
    curses.curs_set(0)
    letters = {}
    height, width = window.getmaxyx()
    window.nodelay(True)
    for t in range(20):
        window.clear()
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
