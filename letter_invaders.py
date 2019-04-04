"Letter invaders game"

from curses import wrapper
from time import sleep
from gamesetup import Game
from gamewindow import Window


def main(screen):
    settings = {'letter_count':0, 'switch':True,
                'gap_step':0, 'gap':7, 'level_req':7}
    global SCORE
    chances, lifecount = 7, 0
    height, width = 30, 65
    letters = Game({})
    screen = Window(screen, height, width)

    while True:
        screen.make_subwindow()
        screen.take_input(letters, settings)
        settings = letters.generate_letter(width, settings)
        letters.move()
        lifecount = letters.count_life(height, lifecount)
        letters.expire_entered()
        screen.draw(letters.dictionary, lifecount, chances)
        if lifecount == chances:
            SCORE = screen.finalscore()
            break
        sleep(0.25)

if __name__ == '__main__':
    try:
        wrapper(main)
        print("You scored {} points.".format(SCORE))
    except KeyboardInterrupt:
        print("Interrupted!")
