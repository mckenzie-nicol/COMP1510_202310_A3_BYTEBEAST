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
hammer_motor = Motor('F')


# # Write your program here.
# def main():
#     """
#     Execute the program.
#     """
# def scanning45():
#     """
#     Scan the area in front of the robot every 45 degrees.If detected an object, the robot will execute bullrush().
#     """
#     while True:
#         motor_pair.move_tank(0.25, 'rotations', -25, 25)
#         for _ in range(2):
#             if distance_sensor.get_distance_cm() in range(35):
#                 bullrush()
#                 break
#             motor_pair.move_tank(0.25, 'rotations', 25, -25)
#         break


# def straight_until_reach_boundary():
#     while distance_sensor.get_distance_cm() not in range(35):
#         while color_sensor.get_reflected_light() > 80:
#             motor_pair.start_tank(45