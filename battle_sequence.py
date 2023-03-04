from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('E')
claw_motor = Motor('D')


# Write your program here.
def scanning45():
    while True:
        motor_pair.move_tank(0.25, 'rotations', -25, 25)
        for _ in range(2):
            if distance_sensor.get_distance_cm() in range(35):
                bullrush()
                break
            motor_pair.move_tank(0.25, 'rotations', 25, -25)
        break


def straight_until_reach_boundary():
    while distance_sensor.get_distance_cm() not in range(35):
        while color_sensor.get_reflected_light() > 80:
            motor_pair.start_tank(45, 45)
            if distance_sensor.get_distance_cm() in range(35):
                bullrush()
                break
        break


def bullrush():
    claw_motor.run_to_position(130, 'shortest path', 30)
    motor_pair.move_tank(3, 'rotations', 100, 100)
    while True:
        motor_pair.move_tank(30, 30)
        if color_sensor.get_reflected_light() < 80:
            claw_motor.run_to_position(355, 'shortest path', 30)
            break


hub.speaker.beep()
claw_motor.run_to_position(355, 'shortest path', 30)
claw_motor.run_to_position(130, 'shortest path', 30)
claw_motor.run_to_position(355, 'shortest path', 30)
motor_pair.move_tank(0.2, 'rotations', 50, 50)

while True:
    scanning45()
    straight_until_reach_boundary()
    motor_pair.move_tank(0.775, 'rotations', -25, 25)