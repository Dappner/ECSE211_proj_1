import brickpi3
import time

BP = brickpi3.BrickPi3()

def stop_motor():
    BP.set_motor_power(BP.PORT_A, 0)

def run_motor():
    cycle = 0
    DELAY = 0.25
    DPS = 720
    while cycle < 20:
        BP.set_motor_dps(BP.PORT_A, DPS)
        time.sleep(DELAY)
        BP.set_motor_dps(BP.PORT_A, -DPS)
        time.sleep(DELAY)
        
        cycle += 1
    stop_motor()

if (__name__ == "__main__"):
    try: 
        run_motor()
    except KeyboardInterrupt:
        stop_motor()
        BP.reset_all()