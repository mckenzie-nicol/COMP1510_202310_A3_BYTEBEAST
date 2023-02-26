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
# The highter the steer_factor, the more drastic corrections the bot will make. Lower steer_factor, the smoother the
# corrections will be.

target = colour.get_reflected_light()
steer_factor = 1

# When initially determining the steer_factor, set error_factor and anticipate_factor to 0. Once the steer_factor is
# determined, adjust error_factor and anticipate_factor.
# Overall, the sum_of_error should be relatively close to zero, as the same errors are expected to happen on either
# side. Negative errors to the left, and positive errors to the right.

error = 0
sum_of_error = 0
error_factor = 0

anticipate_error = 0
last_error = 0
anticipate_factor = 0

# Write your program here.
hub.speaker.beep()
# Ask the distance sensor to take a reading.
distance_sensor.get_distance_cm()
# If no obstacle is detected within 10cm, start the motor and drive in a straight direction. Calculate the light
# difference (% of black tape vs % of other background)
while distance_sensor > 10 or None:
    motor_pair.start()
    light_difference = target - colour.get_reflected_light()
# If the light_difference varies by more than +/- 2, the bot will evaluate the error by subtracting the light_difference
    # from the initial target value.
    while light_difference < -2   or light_difference > 2:
        error = target - light_difference
        sum_of_error += error
        anticipate_error = error - last_error
# The steer_amount is calculated by adding 3 factors. The error, the ongoing sum of errors, and the anticipated error
        # based on the most recent error.
        steer_amount = (error * steer_factor) + (sum_of_error * error_factor) + (anticipate_error * anticipate_factor)
# The current error becomes the last error, and then the bot is steered based on this calculation.
        last_error = 0
        last_error += error
        motor_pair.start(steer_amount)
# The distance sensor is run at the end of the loop and will stop the bot if it encounters an obstacle. If no obstacle
    # is detected, the loop is iterated.
    distance_sensor.get_distance_cm()
