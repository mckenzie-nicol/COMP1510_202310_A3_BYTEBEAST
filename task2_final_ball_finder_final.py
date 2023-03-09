from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('E')
claw_motor = Motor('D')


# Write your program here.
def ball_pickup():
    """
    Capture the ball within the claws.
    """
    motor_pair.move_tank(0.25, 'rotations', 10, 10)
    claw_motor.run_to_position(130, 'shortest path', 30)
    while color_sensor.get_reflected_light() > 80:
        motor_pair.start_tank(20, 20)


def ball_pickup_first_attempt():
    """
    Capture ball within the claws if ball is seen on the first attempt
    """
    motor_pair.move_tank(0.25, 'rotations', 10, 10)
    claw_motor.run_to_position(130, 'shortest path', 30)


def get_radius():
    """
    Obtain the radius of the circle that the robot is in
    """
    rotation_count = 0.2
    while color_sensor.get_reflected_light() > 92 and claw_motor.get_position() > 200:
        motor_pair.move_tank(0.20, 'rotations', 50, 50)
        rotation_count += 0.20
        if distance_sensor.get_distance_cm() in range(10):
            ball_pickup_first_attempt()
    return rotation_count


def reverse_to_center(rotation_count):
    """
    Reverse back to the center of the circle
    """
    motor_pair.move_tank(-(rotation_count), 'rotations', 50, 50)


def initialize():
    """
    Calibrate the claw positions
    """
    hub.speaker.beep()
    claw_motor.run_to_position(355, 'shortest path', 30)
    claw_motor.run_to_position(130, 'shortest path', 30)
    claw_motor.run_to_position(355, 'shortest path', 30)
    motor_pair.move_tank(0.2, 'rotations', 70, 70)


def search_for_ball():
    """
    Search for the ball in the area and reverse to the 
    """
    while claw_motor.get_position() > 200:
        while color_sensor.get_reflected_light() > 92 and claw_motor.get_position() > 200:
            motor_pair.start_tank(50, 50)
            if distance_sensor.get_distance_cm() in range(10):
                ball_pickup()
        reverse_to_center(radius)
        motor_pair.move_tank(0.0625, 'rotations', 25, -25)


def main():
    """
    Execute the Program
    """
    initialize()
    radius = get_radius()
    reverse_to_center(radius)
    motor_pair.move_tank(0.0625, 'rotations', 25, -25)
    search_for_ball()


main()