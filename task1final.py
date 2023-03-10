from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
# from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.

hub = MSHub()
# distance_sensor = DistanceSensor('C')
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(100)
colour = ColorSensor('C')


# Write your program here.
target = 65
steer_factor = 2.7
steer_correct = 0
steer_amount = 0
sum_of_error = 0
integral_factor = 0.0425
last_error = 0
derivative = 0
derivative_factor = 0.03

hub.speaker.beep()

def follow_line():
    """
    Follow the line using a proportional, integral, derivative (PID) algorithm.

    A simple function that was inspired from builderdude35's youtube channel.
    """
    while True:
        light_difference = target - colour.get_reflected_light()
        sum_of_error += light_difference
        error = light_difference
        sum_of_error = round(sum_of_error * integral_factor)
        derivative = round((error - last_error) * derivative_factor)
        steer_correct = round(light_difference * steer_factor)
        steer_amount = (steer_correct + sum_of_error + derivative)
        motor_pair.start(steer_amount, 60)
        last_error = error

def main():
    """
    Execute the program.
    """
    follow_line()

main()