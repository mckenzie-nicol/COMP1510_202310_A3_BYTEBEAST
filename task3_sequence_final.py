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


def start_hammer():
    distance_sensor.light_up_all(100)
    hammer_motor.start(-100)
    hub.speaker.play_sound('Target Acquired')

def move_to_mid():
    motor_pair.move_tank(25, 'cm', 100, 100)
    motor_pair.start_tank(-100, 100)
    hub.speaker.play_sound('Seek and Destroy')

def circle_of_fury():
    motor_pair.start_tank(-100, 100)

def move_around_the_arena():
    while True:
        wait_for_seconds(4)
        motor_pair.stop()
        timer.reset()
        while color_sensor.get_reflected_light() > 70:
            if timer.now() > 1:
                break
            motor_pair.start_tank(50, 50)
        motor_pair.stop()
        hub.speaker.play_sound('Seek and Destroy')
        circle_of_fury()


hub.speaker.beep()
start_hammer()
move_to_mid()
move_around_the_arena()