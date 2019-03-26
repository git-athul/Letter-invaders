from gamesetup import Setup


def test_move():
    "move() should increase the row-value by one"
    letter_dict = Setup({(0, 300): {'char':'r'}, (60, 140):{'char':'x'}})
    moved_dict = {(1, 300):{'char':'r'}, (61, 140):{'char':'x'}}
    assert letter_dict.move() == moved_dict


def test_update_input():
    """
    update_input() should change the dictionary item if entered character
    matches letter in dictionary-value.
    """
    letter_dict = {(0, 300): {'char':'r', 'life':False, 'color':1},
                   (60, 140):{'char':'x', 'life':False, 'color':2}}
    updated_dict = {(0, 300): {'char':'*', 'life':4, 'color':6},
                    (60, 140):{'char':'x', 'life':False, 'color':2}}
    assert Setup(letter_dict).update_input('r') == (updated_dict, True)
    assert Setup(letter_dict).update_input('a') == (letter_dict, False)


def test_update_input_onlyoneletter():
    "update_input() should only change the letter with highest row value"
    letter_dict = Setup({(0, 300): {'char':'r', 'life':False, 'color':1},
                         (60, 140): {'char':'x', 'life':False, 'color':2},
                         (210, 500): {'char':'r', 'life':False, 'color':3},
                         (200, 100): {'char':'r', 'life':False, 'color':4}})

    updated_dict = {(0, 300): {'char':'r', 'life':False, 'color':1},
                    (60, 140): {'char':'x', 'life':False, 'color':2},
                    (210, 500): {'char':'*', 'life':4, 'color':6},     #
                    (200, 100): {'char':'r', 'life':False, 'color':4}}
    assert letter_dict.update_input('r') == (updated_dict, True)


def test_expire_entered():
    "tests whether 'life' is decreasing and expiring for entered"
    letter_dict = Setup({(0, 300): {'char':'*', 'life':3},
                         (210, 500): {'char':'*', 'life':1},
                         (200, 100): {'char':'r', 'life':False}})

    expired_dict = {(0, 300): {'char':'*', 'life':2},
                   (200, 100): {'char':'r', 'life':False}}
    assert letter_dict.expire_entered() == expired_dict


def test_count_life():
    "tests whether count is increasing"
    height = 500
    count = 1
    letter_dict = Setup({(0, 300):{'char':'r', 'life':False},
                         (501, 140):{'char':'x', 'life':False},  #
                         (500, 130):{'char':'x', 'life':3},
                         (210, 500):{'char':'r', 'life':False},
                         (500, 100):{'char':'r', 'life':False}}) 
    assert letter_dict.count_life(height, count) == 2


def test_generate_letter():
    "tests the changes in settings"
    new = Setup({})

    input_settings = {'letter_count':0,
                      'switch':False, #
                      'gap_step':6, #
                      'gap':7,
                      'level_req':10}
    _, output_settings = new.generate_letter(100, input_settings)
    expected = {'letter_count': 0,
                'switch': True, #
                'gap_step': 0, #
                'gap': 7,
                'level_req': 10}
    assert expected == output_settings

    input_settings = {'letter_count':6,
                      'switch':True,
                      'gap_step':0,
                      'gap':7,
                      'level_req':7}
    _, output_settings = new.generate_letter(100, input_settings)
    expected = {'letter_count':0,
                'switch':False,
                'gap_step':1,
                'gap':6,
                'level_req':14}
    assert expected == output_settings
