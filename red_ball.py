from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
distance_sensor = DistanceSensor('D')
colour_motor = Motor('F')
colour_sensor = ColorSensor('E')
arm_motor = Motor('C')

# Write your program here.
hub.speaker.beep()
hub.motion_sensor.reset_yaw_angle()
# return_angle = -180
motor_pair.move(2, 'seconds')
motor_pair.start_tank(5, -5)
distance_sensor.wait_for_distance_closer_than(40)
# while distance_sensor.get_distance_cm() == None or distance_sensor.get_distance_cm() > 30:
#     # distance_to_object = distance_sensor.get_distance_cm()
motor_pair.stop()
motor_pair.set_default_speed(30)
motor_pair.move_tank(10, 'degrees')
motor_pair.start()
if distance_sensor.get_distance_cm() < 10:
    motor_pair.stop()
    colour_motor.run_for_degrees(90)
# #         # if colour_sensor.get_colour() == 'red'
#         arm_motor.run_for_degrees(75)
#     motor_pair.move_tank(distance_to_object, 'cm', -25, -25)
#     while new_orient != orientation:
#         motor_pair.move_tank(30, 'cm', 25, -25)
#     motor_pair.move(-2, 'seconds', steering=0, 100)


