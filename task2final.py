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
hammer_motor = Motor('F')


# Write your program here.
def ball_pickup():
    """
    Capture the ball within the claws.
    """
    motor_pair.move_tank(0.5, 'rotations', 10, 10)
    hammer_motor.run_to_position(50, 'shortest path', 30)
    claw_motor.run_to_position(130, 'shortest path', 30)
    while color_sensor.get_reflected_light() > 80:
        motor_pair.start_tank(20, 20)


def ball_pickup_first_attempt():
    """
    Capture ball within the claws if ball is seen on the first attempt.
    """
    motor_pair.move_tank(0.25, 'rotations', 10, 10)
    hammer_motor.run_to_position(50, 'shortest path', 30)
    claw_motor.run_to_position(130, 'shortest path', 30)


def get_radius():
    """
    Obtain the radius of the circle that the robot is in.
    """
    rotation_count = 0.2
    while color_sensor.get_reflected_light() > 70 and claw_motor.get_position() > 200:
        motor_pair.move_tank(0.20, 'rotations', 20, 20)
        rotation_count += 0.20
        if distance_sensor.get_distance_cm() in range(15):
            ball_pickup_first_attempt()
    return rotation_count


def reverse_to_center(rotation_count):
    """
    Reverse back to the center of the circle.
    """
    motor_pair.move_tank(-(rotation_count), 'rotations', 35, 35)


def initialize():
    """
    Calibrate the claw positions.
    """
    hub.speaker.beep()
    claw_motor.run_to_position(355, 'shortest path', 30)
    claw_motor.run_to_position(130, 'shortest path', 30)
    claw_motor.run_to_position(355, 'shortest path', 30)
    hammer_motor.run_to_position(340, 'shortest path', 30)
    hammer_motor.run_to_position(50, 'shortest path', 30)
    hammer_motor.run_to_position(340, 'shortest path', 30)
    motor_pair.move_tank(0.2, 'rotations', 20, 20)


def search_for_ball(distance_back):
    """
    Search for the ball in the area and reverse back to the center of the circle. 
    """
    while claw_motor.get_position() > 200:
        while color_sensor.get_reflected_light() > 70 and claw_motor.get_position() > 200:
            motor_pair.start_tank(35, 35)
            if distance_sensor.get_distance_cm() in range(15):
                ball_pickup()
        reverse_to_center(distance_back)
        motor_pair.move_tank(0.0625, 'rotations', 25, 0)
        motor_pair.move_tank(0.0625, 'rotations', 0, -25)


def main():
    """
    Execute the program.
    """
    initialize()
    radius = get_radius()
    reverse_to_center(radius)
    motor_pair.move_tank(0.0625, 'rotations', 25, -25)
    search_for_ball(radius)


main()










# while distance_sensor.get_distance_cm() not in range(6) and claw_motor.get_position() > 200:
#     # count how many times the loop runs
#     # main_loop_count += 1
#     while color_sensor.get_reflected_light() > 90 and claw_motor.get_position() > 200:
#         motor_pair.move_tank(0.15, 'rotations', 100, 100)
#         if distance_sensor.get_distance_cm() in range(6):
#             ball_pickup()
#             # breaking point 1
#             # breaking_point = 1
#             break
#     if distance_sensor.get_distance_cm() not in range(6) and claw_motor.get_position() > 200:
#         motor_pair.move_tank(-1.35, 'rotations', 25, 25)
#         motor_pair.move_tank(0.25, 'rotations', 25, 0)
#         motor_pair.move_tank(0.125, 'rotations', 25, 25)
#         motor_pair.move_tank(0.125, 'rotations', 25, 25)
#     while color_sensor.get_reflected_light() > 90 and claw_motor.get_position() > 200:
#         motor_pair.move_tank(0.075, 'rotations', 9, 15)
#         if distance_sensor.get_distance_cm() in range(10):
#             ball_pickup()
#             # breaking point 2
#             # breaking_point = 2
#         if color_sensor.get_reflected_light() < 90:
#             break
#     motor_pair.move_tank(1, 'rotations', -25, 25)
#     while color_sensor.get_reflected_light() > 90 and claw_motor.get_position() > 200:
#         motor_pair.move_tank(0.15, 'rotations', 100, 100)
#         if distance_sensor.get_distance_cm() in range(6):
#             ball_pickup()
#             # breaking point 3
#             # breaking_point = 3
#             break
#     if distance_sensor.get_distance_cm() not in range(6) and claw_motor.get_position() > 200:
#         motor_pair.move_tank(-1.35, 'rotations', 25, 25)
#         motor_pair.move_tank(0.25, 'rotations', 0, 25)
#         motor_pair.move_tank(0.125, 'rotations', 25, 25)
#         motor_pair.move_tank(0.125, 'rotations', 25, 25)

#     while color_sensor.get_reflected_light() > 90 and claw_motor.get_position() > 200:
#         motor_pair.move_tank(0.075, 'rotations', 15, 9)
#         if distance_sensor.get_distance_cm() in range(10):
#             ball_pickup()
#             # breaking point 4
#             # breaking_point = 4
#         if color_sensor.get_reflected_light() < 90:
#             break
#     motor_pair.move_tank(1, 'rotations', 25, -25)

    # after it finds the ball and breaks out of this loop, we can check to the value of main_loop_count
    # and check to see the value of breaking point so we know exactly how many rotations it took to find the ball
    # then retrace its steps to get back to the starting point
