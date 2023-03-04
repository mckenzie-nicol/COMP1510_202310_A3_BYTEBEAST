from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.

hub = MSHub()
# distance_sensor = DistanceSensor('C')
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(30)
colour = ColorSensor('C')



# Write your program here.
target = 62
steer_factor = 1.25
steer_correct = 0
steer_amount = 0
sum_of_error = 0
integral_factor = 0.7
last_error = 0
derivative = 0
derivative_factor = 2

hub.speaker.beep()
while True:
    light_difference = target - colour.get_reflected_light()
    sum_of_error += light_difference
    error = light_difference
    sum_of_error = round(sum_of_error * integral_factor)
    derivative = round((error - last_error) * derivative_factor)
    steer_correct = round(light_difference * steer_factor)
    steer_amount = steer_correct + sum_of_error + derivative
    motor_pair.start(steer_amount, 30)
    last_error = error

