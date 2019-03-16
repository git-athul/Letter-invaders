import gamelogic


def test_move():
    init_dict = {(0, 300):'r', (60,140):'x'}
    moved_dict = {(1, 300):'r', (61,140):'x'}
    assert gamelogic.move(init_dict) == moved_dict    

def test_kill():
    init_dict = {(0, 300):'r', (60,140):'x'}
    killed_dict = {(60,140):'x'}
    assert gamelogic.kill(init_dict, 'r') == killed_dict
    assert gamelogic.kill(init_dict, 'a') == init_dict
