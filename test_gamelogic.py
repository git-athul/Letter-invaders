import gamelogic


def test_move_invaders():
    init_dict = {'r':(0, 300), 'x':(60,140)}
    moved_dict = {'r':(1, 300), 'x':(61,140)}
    assert gamelogic.move(init_dict) == moved_dict
