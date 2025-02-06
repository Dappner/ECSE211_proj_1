
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensor
import time
SOUND = sound.Sound(duration=0.3, pitch="A4", volume=60)
TOUCH_SENSOR = TouchSensor()

wait_ready_sensor(TOUCH_SENSOR)

def play_sound():
    SOUND.play()
    SOUND.wait_done()

def play_sound_on_button_press():
    try:
        print("test")
    except:
        print("error")
    time.sleep(0.02)

if __name__ == '__main__':
    play_sound_on_button_press()