from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
# from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('E')
claw_motor = Motor('D')
hammer_motor = Motor('F')
timer = Timer()


def start_cyclone_of_death():
    """
    Energize front weaponry.
    """
    distance_sensor.light_up_all(100)
    hammer_motor.start(-100)


def move_to_mid():
    """
    Charge to the middle of the arena.
    """
    motor_pair.move_tank(25, 'cm', 100, 100)
    motor_pair.start_tank(-100, 100)


def circle_of_fury():
    """
    Pivot the robot at full speed in a circle.
    """
    motor_pair.start_tank(-100, 100)


def move_around_the_arena():
    """
    Move around the circle in designated time intervals.
    """
    while True:
        wait_for_seconds(4)
        motor_pair.stop()
        timer.reset()
        while color_sensor.get_reflected_light() > 70:
            if timer.now() > 1:
                break
            motor_pair.start_tank(50, 50)
        motor_pair.stop()
        circle_of_fury()


def main():
    """
    Execute the program.
    """
    hub.speaker.beep()
    start_cyclone_of_death()
    move_to_mid()
    move_around_the_arena()


main()

