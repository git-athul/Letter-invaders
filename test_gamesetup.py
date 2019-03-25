from gamesetup import Setup


def test_move():
    "move() should increase the row-value by one"
    letter_dict = Setup({(0, 300): {'char':'r'}, (60, 140):{'char':'x'}})
    moved_dict = {(1, 300):{'char':'r'}, (61, 140):{'char':'x'}}
    assert letter_dict.move() == moved_dict

def test_input_update():
    """
    input_update() should change the dictionary item if entered character
    matches letter in dictionary-value.
    """
    letter_dict = {(0, 300): {'char':'r', 'life':False}, (60, 140):{'char':'x', 'life':False}}
    updated_dict = {(0, 300): {'char':'*', 'life':4}, (60, 140):{'char':'x', 'life':False}}
    assert Setup(letter_dict).input_update('r') == updated_dict
    assert Setup(letter_dict).input_update('a') == letter_dict

def test_input_update_onlyoneletter():
    "input_update() should only change the letter with highest row value"
    letter_dict = Setup({(0, 300): {'char':'r', 'life':False},
                         (60, 140): {'char':'x', 'life':False},
                         (210, 500): {'char':'r', 'life':False},
                         (200, 100): {'char':'r', 'life':False}})

    updated_dict = {(0, 300): {'char':'r', 'life':False},
                    (60, 140): {'char':'x', 'life':False},
                    (210, 500): {'char':'*', 'life':4},     #
                    (200, 100): {'char':'r', 'life':False}}
    assert letter_dict.input_update('r') == updated_dict

def test_kill():
    """Decreases the life if it is number, and then
    removes the item when life is equal to zero"""
    letter_dict = Setup({(0, 300): {'char':'*', 'life':3},
                         (210, 500): {'char':'*', 'life':1},
                         (200, 100): {'char':'r', 'life':False}})

    killed_dict = {(0, 300): {'char':'*', 'life':2},
                   (200, 100): {'char':'r', 'life':False}}
    assert letter_dict.kill() == killed_dict


def test_life():
    "Checks how many letters have passed the 'height'"
    height = 500
    letter_dict = Setup({(0, 300):{'char':'r', 'life':False},
                         (500, 140):{'char':'x', 'life':False},  #
                         (500, 130):{'char':'x', 'life':3},
                         (210, 500):{'char':'r', 'life':False},
                         (500, 100):{'char':'r', 'life':False}}) #
    assert letter_dict.life(height) == 2
