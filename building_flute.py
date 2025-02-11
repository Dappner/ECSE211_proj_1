from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, Motor
import time
# from dataclasses import dataclass, field


# @dataclass
# class Note:
#     sensor: TouchSensor
#     label: str
#     sound: sound.Sound
#     last_play_time: float = field(default_factory=lambda: 0.0)


class Flute:
    def __init__(self):
        # Initialize Flute Sensors
        self.touch_sensor_1 = TouchSensor(3)
        self.touch_sensor_2 = TouchSensor(4)
        self.touch_sensor_3 = TouchSensor("D")

        # sensor to start stop
        self.stop_sensor = TouchSensor()

        # Motor Port
        self.motor = Motor("")

        self.drums_playing = False

        # Wait for sensors to be ready
        wait_ready_sensors()

        self.notes = [
            {
                "sensor": self.touch_sensor_1,
                "label": "Note C",
                "sound": sound.Sound(duration=1, pitch="C4", volume=100),
                "last_play_time": 0,
            },
            {
                "sensor": self.touch_sensor_2,
                "label": "Note E",
                "sound": sound.Sound(duration=1, pitch="E4", volume=100),
                "last_play_time": 0,
            },
            {
                "sensor": self.touch_sensor_3,
                "label": "Note F",
                "sound": sound.Sound(duration=1, pitch="F4", volume=100),
                "last_play_time": 0,
            },
        ]

        # Chords
        self.chords = [
            {
                "sensors": [self.touch_sensor_1, self.touch_sensor_2],
                "label": "Chord G4",
                "sound": sound.Sound(duration=1, pitch="G4", volume=100),
                "last_play_time": 0,
            }
        ]

        # Set minimum time between sound plays (in seconds)
        self.play_interval = 0.4

    def main_loop(self):
        """Main loop to handle button presses and play sounds"""
        self.print_instructions()
        # Loop
        while True:
            chord_played = False

            # Check for start tstop
            if self.stop_sensor.is_pressed():
                self.toggle_drums()
                # Wait until it is released
                while self.stop_sensor.is_pressed():
                    time.sleep(0.1)

            # Check for Chord
            for chord in self.chords:
                # Checks to see if all sensors in code are pressed
                if all(sensor.is_pressed() for sensor in chord["sensors"]):
                    # If can play, returns play time
                    play_time = self.can_play_sound(chord["last_play_time"])
                    if play_time:
                        print(f"Playing {chord['label']}")
                        chord["sound"].play()
                        chord["last_play_time"] = play_time
                        # If a chord is played, you want to skip individual notes this cycle.
                        chord_played = True
                        break

            # Check for individual notes
            if not chord_played:
                for note in self.notes:
                    if note["sensor"].is_pressed():
                        play_time = self.can_play_sound(note["last_play_time"])
                        if play_time:
                            note["sound"].play()
                            note["last_play_time"] = play_time

            time.sleep(0.02)

    def print_instructions(self):
        print("Flute is ready! Press touch sensors to play sounds.")
        print("- Touch Sensor 1: C4")
        print("- Touch Sensor 2: E4")
        print("- Touch Sensor 3: F4")
        print("  Touch Sensors 1 & 2 : G4")

    def toggle_drums(self):
        self.drums_playing = not self.drums_playing
        if self.drums_playing:
            self.motor.set_power(20)
        else:
            self.motor.set_power(0)

    # Returns current time if can play, otherwise returns none
    def can_play_sound(self, last_play_time):
        """Check if enough time has passed to play a sound again"""
        current_time = time.time()
        if current_time - last_play_time >= self.play_interval:
            return current_time
        return None

    def reset_sensors(self):
        self.motor.set_power(0)


def main():
    flute = Flute()
    try:
        flute.main_loop()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print("\nAn error occurred: ", e)
    finally:
        flute.reset_sensors()


if __name__ == "__main__":
    main()

