from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors
import time


SOUND_1 = sound.Sound(duration=0.3, pitch="C4", volume= 100)
SOUND_2 = sound.Sound(duration=0.3, pitch="D4", volume= 100)

TOUCH_SENSOR_1 = TouchSensor(3)
TOUCH_SENSOR_2 = TouchSensor(4)


wait_ready_sensors()

def play_sound_1():
    SOUND_1.play()
    SOUND_1.wait_done()

def play_sound_2():
    SOUND_2.play()
    SOUND_2.wait_done()

def play_combined_sound():
    SOUND_3 = SOUND_1.append(SOUND_2).play()
    SOUND_3.wait_done()


def play_sound_on_button_press():
    try:
        while True:
            if TOUCH_SENSOR_1.is_pressed() and TOUCH_SENSOR_2.is_pressed():
                play_combined_sound()
            if TOUCH_SENSOR_1.is_pressed():
                play_sound_1()
            if TOUCH_SENSOR_2.is_pressed():
                play_sound_2()

            time.sleep(0.02)  

    except KeyboardInterrupt:
        print("Program stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    play_sound_on_button_press()
