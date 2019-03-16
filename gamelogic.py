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

def kill(dictionary, input_letter):
    """
    Removes an item of the lowest letter from the dictionary, that matches to
    input_letter. The lowest letter will have the highest row value.
    """
    low = -1
    low_key = False
    for location, letter in dictionary.items():
        if letter is input_letter:
            if low < location[0]:
                low = location[0]
                low_key = location
    if low_key:
        del dictionary[low_key]
    return dictionary
