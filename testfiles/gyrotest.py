from __future__ import print_function
from __future__ import division

import time
import brickpi3

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)

try:
    while True:
        try:
            gyro_value = (BP.get_sensor(BP.PORT_2))
            print([gyro_value[0] % 360], gyro_value[1])
        except brickpi3.SensorError as error:
            print(error)


        time.sleep(0.02)
except KeyboardInterrupt:
    BP.reset_all()