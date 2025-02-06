from brickpi3 import BrickPi3
from time import sleep
import simpleaudio as sa
import time

# Initialize BrickPi
BP = BrickPi3()

# Define touch sensor ports (adjust port numbers as needed)
TOUCH_PORT_1 = BP.PORT_1
TOUCH_PORT_2 = BP.PORT_2

# Create sound objects (using simpleaudio for sound)
def create_sound(freq=440, duration=0.3):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(2 * np.pi * freq * t)
    audio = np.int16(tone * 32767)
    return sa.WaveObject(audio, 1, 2, sample_rate)

SOUND_1 = create_sound(freq=261.63)  # C4
SOUND_2 = create_sound(freq=293.66)  # D4

def play_sound_1():
    play_obj = SOUND_1.play()
    play_obj.wait_done()

def play_sound_2():
    play_obj = SOUND_2.play()
    play_obj.wait_done()

def play_sound_on_button_press():
    try:
        while True:
            try:
                # Read touch sensor values
                sensor1 = BP.get_sensor(TOUCH_PORT_1)
                sensor2 = BP.get_sensor(TOUCH_PORT_2)
                
                if sensor1:
                    play_sound_1()
                if sensor2:
                    play_sound_2()
                    
                time.sleep(0.02)  # Small delay to prevent CPU overuse
                
            except BrickPi3.SensorError:
                pass  # Handle sensor read errors gracefully
                
    except KeyboardInterrupt:
        print("Program stopped by user")
        BP.reset_all()  # Reset BrickPi
    except Exception as e:
        print(f"An error occurred: {e}")
        BP.reset_all()  # Reset BrickPi

if __name__ == '__main__':
    try:
        # Configure sensors as touch
        BP.set_sensor_type(TOUCH_PORT_1, BP.SENSOR_TYPE.TOUCH)
        BP.set_sensor_type(TOUCH_PORT_2, BP.SENSOR_TYPE.TOUCH)
        time.sleep(0.5)  # Give sensors time to initialize
        
        play_sound_on_button_press()
        
    except Exception as e:
        print(f"Initialization error: {e}")
    finally:
        BP.reset_all()  # Always reset BrickPi when done