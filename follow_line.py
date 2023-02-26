from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()
distance_sensor = DistanceSensor('A')
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(50)
colour = ColorSensor('E')
# When bot sensor is placed on 50% black and 50% other colour, the amount of reflected light becomes our target.
# The highter the steer_factor, the more drastic corrections the bot will make. Lower steer_factor, the smoother the corrections will be.

target = colour.get_reflected_light()
steer_factor = 1

error = 0

# Write your program here.
hub.speaker.beep()
# Ask the distance sensor to take a reading.
distance_sensor.get_distance_cm()
# If no obstacle is detected within 10cm, start the motor and drive in a straight direction. Calculate the light difference (% of black tape vs % of other background)
while distance_sensor > 10 or None:
    motor_pair.start()
    light_difference = target - colour.get_reflected_light()
    # If the light_differnce varies by more than +/- 2, the bot will evaluate the error by subtracting the light_difference from the inital target value.
    while light_difference < -2 or light_difference > 2:
        error = target - light_difference
        # The steer_amount is calculated the error multiplied by the steering factor.
        steer_amount = error * steer_factor
        motor_pair.start(steer_amount)
    # The distance sensor is run at the end of the loop and will stop the bot if it encounters an obstacle. If no obstacle is detected, the loop is iterated.
    distance_sensor.get_distance_cm()
