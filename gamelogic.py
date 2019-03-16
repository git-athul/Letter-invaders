"Functions for Letter invaders game"

import random
import string


def new_letter(width, dictionary):
    "Generates new letter and adds to dictionary"
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(5, width)
    new = {(0, column):letter}
    dictionary.update(new)
    return dictionary

def move(dictionary):
    "Moves letters down"
    moved = {}
    for (row, column), letter in dictionary.items():
        moved[(row + 1, column)] = letter
    return moved
