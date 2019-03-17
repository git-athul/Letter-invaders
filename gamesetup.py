"Functions for Letter invaders game"

import random
import string

class Setup(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def new_letter(self, width):
        "Generates new letter and adds to dictionary"
        key =  (1, random.randrange(1, width))
        char = random.choice(string.ascii_lowercase)
        color = random.randrange(3, 7)
        value = {'char':char, 'color':color}
        self.dictionary[key] = value
        return self.dictionary

    def move(self):
        "Moves letters down by increasing value of row"
        moved = {}
        for (row, column), value in self.dictionary.items():
            moved[(row + 1, column)] = value
        return moved

    def kill(self, input_letter):
        """
        If 'input_letter' matches to any 'char' from dictionary, removes
        the item with highest row among matches.
        """
        row = -1
        row_key = False
        for location, letter in self.dictionary.items():
            if letter['char'] is input_letter:
                if row < location[0]:
                    row = location[0]
                    row_key = location
        if row_key:
            del self.dictionary[row_key]
        return self.dictionary

    def life(self, height):
        "Checks how many letters have passed the 'height'"
        count = 0
        for (row, _), _ in self.dictionary.items():
            if row >= height:
                count += 1
        return count
