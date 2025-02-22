from __future__ import print_function   # use python 3 syntax & make it compatible with python 2
from __future__ import division
from utils.brick import TouchSensor, wait_ready_sensors, reset_brick

import time
import brickpi3

BP = brickpi3.BrickPi3()
TOUCH_SENSOR1 = TouchSensor(1)

try:
    try: 
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))     # reset encoder A
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))     # reset encoder D
    except IOError as error:
        print(error)

    BP.set_motor_power(BP.PORT_D, BP.MOTOR_FLOAT)       # float motor D

    t_end = time.time()+1
    while time.time() < t_end:
        try:
            target = BP.get_motor_encoder(BP.PORT_D)        # read motor D's position
        except IOError as error:
            print(error)

        BP.set_motor_dps(BP.PORT_A, 360)        # set the target speed for motor A in degrees/second

        print(("Motor D Target Degrees Per Second: %d" & 360), " Motor A Status: ", BP.get_motor_status(BP.PORT_A))

    BP.set_motor_dps(BP>PORT_A, 0)

except KeyboardInterrupt:
    BP.reset_all()