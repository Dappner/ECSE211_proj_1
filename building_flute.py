from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors
import time

class Flute:
    def __init__(self):
        # Initialize touch sensors
        self.touch_sensor_1 = TouchSensor(3)  # Port 3
        self.touch_sensor_2 = TouchSensor(4)  # Port 4
        
        # Wait for sensors to be ready
        wait_ready_sensors()
        
        # Initialize sounds
        self.note_c = sound.Sound(duration=0.5, pitch = "C4", volume=100)
        self.note_e = sound.Sound(duration=0.5, pitch = "E4", volume=100)
        self.note_g = sound.Sound(duration=0.5, pitch = "G4", volume=100)


        # Track last play time for each sound
        self.last_play_time_1 = 0
        self.last_play_time_2 = 0
        self.last_play_time_1&2 = 0
        
        # Set minimum time between sound plays (in seconds)
        self.play_interval = 0.4  # Adjust this to control how frequently sounds can play
        
    def can_play_sound(self, last_play_time):
        """Check if enough time has passed to play a sound again"""
        current_time = time.time()
        if current_time - last_play_time >= self.play_interval:
            return current_time
        return None
    
    def play_sound_on_button_press(self):
        """Main loop to handle button presses and play sounds"""
        print("Flute is ready! Press touch sensors to play sounds.")
        print("- Touch Sensor 1: C4")
        print("- Touch Sensor 2: E4")
        print("- Both Sensors: C major chord (C4 + E4)")
        
        try:
            while True:
                current_time = time.time()
                
                # Check button states
                button1 = self.touch_sensor_1.is_pressed()
                button2 = self.touch_sensor_2.is_pressed()
                
                # Handle both buttons pressed - play chord
                if button1 and button2:
                    play_time = self.can_play_sound(self.last_play_time_1&2)
                    if play_time:
                        print("Playing G4")
                        self.note_g.play()
                        self.last_play_time_1&2 = play_time
                
                # Handle individual buttons if not playing chord
                else:
                    if button1:
                        play_time = self.can_play_sound(self.last_play_time_1)
                        if play_time:
                            print("Playing C4")
                            self.note_c.play()
                            self.last_play_time_1 = play_time
                    
                    if button2:
                        play_time = self.can_play_sound(self.last_play_time_2)
                        if play_time:
                            print("Playing E4")
                            self.note_e.play()
                            self.last_play_time_2 = play_time
                
                # Small delay to prevent CPU overuse
                time.sleep(0.02)
                
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

def main():
    flute = Flute()
    flute.play_sound_on_button_press()

if __name__ == '__main__':
    main()