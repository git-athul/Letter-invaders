"Functions for Letter invaders game"

import random
import string

class Setup():

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def new_letter(self, width):
        "Generates new letter and adds to dictionary"
        key = (1, random.randrange(1, width))
        char = random.choice(string.ascii_lowercase)
        color = random.randrange(1, 6)
        value = {'char':char, 'color':color, 'life':False}
        self.dictionary[key] = value
        return self.dictionary

    def letter_generator(self, width, letter_count,
                         gap_step, gap, switch, level_req):
        "Generates letters in increasing frequency"
        if switch:
            Setup.new_letter(self, width)
            letter_count += 1
            switch = False
        gap_step += 1
        if gap == gap_step or gap == 1:
            switch = True
            gap_step = 0
        if letter_count == level_req:
            letter_count = 0
            level_req += 7
            if gap != 1:
                gap -= 1
        return self.dictionary, letter_count, gap_step, gap, switch, level_req

    def move(self):
        "Moves letters down by increasing value of row"
        moved = {}
        for (row, column), value in self.dictionary.items():
            moved[(row + 1, column)] = value
        return moved

    def input_update(self, input_letter):
        """
        If 'input_letter' matches to any 'char' from dictionary, changes
        the value of item with highest row among matches.
        """
        row = -1
        row_key = False
        score = False
        for location, letter in self.dictionary.items():
            if letter['char'] is input_letter:
                if row < location[0]:
                    row = location[0]
                    row_key = location

        if row_key:
            letter = self.dictionary[row_key]
            letter['char'] = "*"
            letter['life'] = 4
            score = True
        return self.dictionary, score

    def kill(self):
        """
        Decreases the life if it is number, and then
        removes the item when life is equal to zero
        """

        del_key = []
        for location, letter in self.dictionary.items():
            if letter['life']:
                letter['life'] -= 1
                if letter['life'] == 0:
                    del_key.append(location)
        while del_key:
            del self.dictionary[del_key[0]]
            del_key.pop(0)
        return self.dictionary

    def life(self, height):
        "Checks how many letters have passed the 'height'"
        count = 0
        for (row, _), letter in self.dictionary.items():
            if row >= height and not letter['life']:
                count += 1
        return count
