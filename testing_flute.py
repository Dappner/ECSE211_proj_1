from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3ColorSensor
import time

class Flute:
    def __init__(self):
        # Initialize touch sensors
        self.touch_sensor_1 = TouchSensor(3)  # Port 3
        self.touch_sensor_2 = TouchSensor(4)  # Port 4
        
        # Initialize base sounds
        self.sound_1 = sound.Sound(duration=0.3, pitch="C4", volume=40)  # Lower individual volumes
        self.sound_2 = sound.Sound(duration=0.3, pitch="E4", volume=40)  # for better chord balance
        
        # Create chord sound (C major)
        self.chord_sound = sound.Sound(duration=0.3, pitch="C4", volume=40)
        self.chord_sound.append(sound.Sound(duration=0.3, pitch="E4", volume=40))
        
        # Wait for sensors to be ready
        wait_ready_sensors()
        
        # Track sound states
        self.sound_1_playing = False
        self.sound_2_playing = False
        self.chord_playing = False
        
    def start_sound_1(self):
        """Start playing the first sound (C4) if not already playing"""
        if not self.sound_1_playing:
            self.sound_1.play()
            self.sound_1_playing = True
            
    def start_sound_2(self):
        """Start playing the second sound (E4) if not already playing"""
        if not self.sound_2_playing:
            self.sound_2.play()
            self.sound_2_playing = True
            
    def start_chord(self):
        """Start playing the chord if not already playing"""
        if not self.chord_playing:
            self.chord_sound.play()
            self.chord_playing = True
            
    def stop_sound_1(self):
        """Stop the first sound if playing"""
        if self.sound_1_playing:
            self.sound_1.stop()
            self.sound_1_playing = False
            
    def stop_sound_2(self):
        """Stop the second sound if playing"""
        if self.sound_2_playing:
            self.sound_2.stop()
            self.sound_2_playing = False
            
    def stop_chord(self):
        """Stop the chord if playing"""
        if self.chord_playing:
            self.chord_sound.stop()
            self.chord_playing = False
            
    def stop_all_sounds(self):
        """Stop all sounds"""
        self.stop_sound_1()
        self.stop_sound_2()
        self.stop_chord()
        
    def play_sound_on_button_press(self):
        """Main loop to handle button presses and play sounds continuously"""
        print("Flute is ready! Hold touch sensors to play sounds.")
        print("- Touch Sensor 1: C4")
        print("- Touch Sensor 2: E4")
        print("- Both Sensors: C major chord (C4 + E4)")
        
        try:
            while True:
                # Get current button states
                button1_pressed = self.touch_sensor_1.is_pressed()
                button2_pressed = self.touch_sensor_2.is_pressed()
                
                # Handle chord (both buttons)
                if button1_pressed and button2_pressed:
                    self.stop_sound_1()
                    self.stop_sound_2()
                    self.start_chord()
                else:
                    # Handle individual buttons
                    self.stop_chord()
                    
                    if button1_pressed:
                        self.start_sound_1()
                    else:
                        self.stop_sound_1()
                        
                    if button2_pressed:
                        self.start_sound_2()
                    else:
                        self.stop_sound_2()
                
                time.sleep(0.02)  # Small delay to prevent CPU overuse
                
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            self.stop_all_sounds()
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            self.stop_all_sounds()

def main():
    flute = Flute()
    flute.play_sound_on_button_press()

if __name__ == '__main__':
    main()