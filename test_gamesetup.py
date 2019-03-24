from gamesetup import Setup


def test_move():
    "move() should increase the row-value by one"
    letter_dict = Setup({(0, 300): {'char':'r'}, (60,140):{'char':'x'}})
    moved_dict = {(1, 300):{'char':'r'}, (61,140):{'char':'x'}}
    assert letter_dict.move() == moved_dict    

def test_kill():
    """
    kill() should remove the dictionary item if entered character
    matches letter in dictionary-value.
    """
    letter_dict = {(0, 300): {'char':'r'}, (60,140):{'char':'x'}}
    killed_dict = {(60,140):{'char':'x'}}
    assert Setup(letter_dict).kill('r') == killed_dict
    assert Setup(letter_dict).kill('a') == letter_dict

def test_kill_onlyoneletter():
    "kill() should only remove the letter with highest row value"
    letter = {(0, 300): {'char':'r'}, (60,140): {'char':'x'}, (210, 500): {'char':'r'}, (200, 100): {'char':'r'}}
    letter_dict = Setup(letter)
    killed_dict = {(0, 300): {'char':'r'}, (60,140): {'char':'x'}, (200, 100): {'char':'r'}}
    assert letter_dict.kill('r') == killed_dict

def test_life():
    height = 500
    letter_dict = Setup({(0, 300):'r', (500,140):'x', (210, 500):'r', (500, 100):'r'})
    assert letter_dict.life(height) == 2
