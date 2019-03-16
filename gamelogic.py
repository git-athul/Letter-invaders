"Functions for Letter invaders game"

import random
import string


def new_letter(width, dictionary):
    "Generates new letter and adds to dictionary"
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(5, width)
    new = {letter :  (0, column)}
    dictionary.update(new)
    return dictionary

def move(dictionary):
    "Moves letters down"
    moved = {}
    for letter, (row, column) in dictionary.items():
        moved[letter] = (row + 1, column)
    return moved
