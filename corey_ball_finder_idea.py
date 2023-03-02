from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
movement_motors = MotorPair('A', 'B')
# colour_sensor = ColorSensor('E')
distance_sensor = DistanceSensor('D')
lifting_arm = Motor('C')
# Write your program here.
hub.speaker.beep()

rotation_count = 0
right_turns = 0
movement_motors.set_default_speed(30)
NoneType_value = None
do_nothing = 0

def move_forward():
    movement_motors.move(1, 'rotations', steering=0)
    rotation_count += 1

def right_turn():
    movement_motors.move_tank(10, 'cm', 30, 0)
    right_turns += 1

def reverse_right_turn():
    movement_motors.move_tank(-10, 'cm', 30, 0)
    right_turns -= 1

def move_backward():
    movement_motors.move(-1, 'rotations', steering=0)
    rotation_count -= 1

while True:
    move_forward()
    get_distance = distance_sensor.get_distance_cm()
    if get_distance == NoneType_value:
        do_nothing += 1
    else: 
        if get_distance < 30:
            movement_motors.set_default_speed(20)
            move_forward()
            lifting_arm.run_to_position(270, 'shortest path', 10)
            right_turn()
            movement_motors.set_default_speed(70)
            break
    right_turn()

while rotation_count > 0 or right_turns > 0:
    reverse_right_turn()
    move_backward()