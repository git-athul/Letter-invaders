from gamelogic import *


def draw(dictionary, window):
    "Draws dictionary in window!"
    for letter, (row, column) in dictionary.items():
        window.addch(row, column, letter)
