import brickpi3
import time
from utils import sound

BP = brickpi3.BrickPi3()

SOUND = sound.Sound(duration=0.3, pitch="A4", volume=60)

def play_sound():
    SOUND.play()
    SOUND.wait_done()


def play_loop():



    pass



if __name__ == '__main__':
    try: 
        play_loop()
    except KeyboardInterrupt:
        BP.reset_all()