from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
timer = Timer()
# wait = wait()
# setting this motorpair to b and a means the robot moving backward is the new forward movement so we don't have to reverse all our values down below
movement_motors = MotorPair('A', 'B')
colour_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('D')

movement_motors.set_default_speed(30)

# timer = 0
while True:
    # can add a multiplier for if the course designed has really sharp turn, if you multiply the number within the brackets it will cause the robot to correct itself with a sharper turn 
    
    if colour_sensor.get_color() == 'black':
        movement_motors.start()
    else:
        
    light_value = colour_sensor.get_reflected_light()
    if colour_sensor.get_color() == 'green':
        movement_motors.stop()
        break