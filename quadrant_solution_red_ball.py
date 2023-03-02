from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_a = Motor('A')
motor_b = Motor('B')
motor_pair = MotorPair('A', 'B')
distance_sensor = DistanceSensor('D')
arm_motor = Motor('C')
timer = Timer()
colour_sensor = ColorSensor('E')
entry_area = 0
width_centered = 0
length_centered = 0


# Write your program here.
def bot_scan_area():
    while distance_sensor.get_distance_cm() not in range(31):
        motor_pair.start(5, -5)
        while hub.motion_sensor.get_yaw_angle() != -1:
            continue
        break
    ball_pickup()


def ball_pickup():
    distance_to_object = distance_sensor.get_distance_cm()
    while distance_sensor.get_distance_cm() not in range(5):
        motor_pair.start()
    motor_pair.stop()
    arm_motor.run_to_position(290, 'shortest path', 10)
    motor_pair.move((distance_to_object * -1), 'cm')


def first_quadrant():
    while distance_sensor.get_distance_cm() not in range(31):
        motor_pair.move(-5, 5)
        while hub.motion_sensor.get_yaw_angle() >= -90:
            continue
        motor_pair.move((round(width_centered / 2)), 'seconds')
        while hub.motion_sensor.get_yaw_angle() >= -178:
            continue
        motor_pair.move((round(length_centered / 2)), 'seconds')
        motor_pair.move(-5, 5)
        while hub.motion_sensor.get_yaw_angle() <= 0:
            continue
        break


def second_quadrant():
    while distance_sensor.get_distance_cm() not in range(31):
        motor_pair.move(length_centered, 'seconds')
        break


def third_quadrant():
    while distance_sensor.get_distance_cm() not in range(31):
        motor_pair.move(-5, 5)
        while hub.motion_sensor.get_yaw_angle() <= 90:
            continue
        motor_pair.move(width_centered, 'seconds')
        break


def fourth_quadrant():
    while distance_sensor.get_distance_cm() not in range(31):
        motor_pair.move(-5, 5)
        while hub.motion_sensor.get_yaw_angle() <= -178:
            continue
        motor_pair.move(length_centered, 'seconds')
        break


def go_home():
    motor_pair.start(5, -5)
    while hub.motion_sensor.get_yaw_angle() != 90:
        continue
    motor_pair.start()
    while colour_sensor.get_colour != 'black':
        continue
    while hub.motion_sensor.get_yaw_angle() >= -178:
        motor_b.start(-20)
    motor_pair.start()
    while colour_sensor.get_colour != 'black':
        continue
    while hub.motion_sensor.get_yaw_angle() <= -90:
        motor_b.start(-20)
    motor_pair.move(entry_area, 'seconds')
    motor_pair.start(-5, 5)
    while hub.motion_sensor.get_yaw_angle() >= 178:
        continue
    motor_pair.move(1, 'rotations')


hub.speaker.beep()
hub.motion_sensor.reset_yaw_angle()
while distance_sensor.get_distance_cm() not in range(31):
    motor_pair.start()
    timer.reset()
    while colour_sensor.get_colour != 'black':
        continue
    motor_pair.stop()
    length_centered = round(timer.now() / 2)
    motor_pair.move((length_centered * -1), 'seconds')
    motor_pair.start(10, -10)
    while hub.motion_sensor.get_yaw_angle() <= 90:
        continue
    motor_pair.start()
    timer.reset()
    while colour_sensor.get_colour != 'black':
        continue
    motor_pair.stop()
    entry_area = timer.now()
    while hub.motion_sensor.get_yaw_angle() >= 0:
        motor_b.start(-20)
    while hub.motion_sensor.get_yaw_angle() <= -90:
        motor_a.start(20)
    motor_pair.start()
    timer.reset()
    while colour_sensor.get_colour != 'black':
        continue
    motor_pair.stop()
    width_centered = round(timer.now() / 2)
    motor_pair.move((width_centered * -1), 'seconds')
    motor_pair.start(10, -10)
    while hub.motion_sensor.get_yaw_angle() <= 0:
        continue
    break
bot_scan_area()
if arm_motor.get_position() < 270:
    first_quadrant()
bot_scan_area()
if arm_motor.get_position() < 270:
    second_quadrant()
bot_scan_area()
if arm_motor.get_position() < 270:
    third_quadrant()
bot_scan_area()
if arm_motor.get_position() < 270:
    fourth_quadrant()
bot_scan_area()
go_home()
