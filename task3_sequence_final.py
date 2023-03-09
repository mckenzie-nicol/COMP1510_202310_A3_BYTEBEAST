This program controls LEGO MINDSTORMS Robot to move around an arena using various sensors.
"""
def function_start_hammer():
   Starts the hammer motor and plays a sound when the distance sensor detects an object.

def function_move_to_mid():
    Moves the robot to the center of the arena while playing a sound.

def function_move_to_mid():
    Starts the motors to make the robot spin in a circle.

def function_move_around_the_arena():
    Makes the robot move around the arena, stopping when it detects a white object and starting again after waiting for a fixed amount of time.

def function_MSHub():

    Access the features of the MINDSTORMS Hub

def function_Motor():
    controll a single motor

    :param port : A sting form ("A","B","C","D","E","F") as the port wichi the motor is connected to on the hub.
    :param speed :  An integer as speed of the motor, from -100 to 100.
    :param angle : An integer as  angle of the motor, in degrees.

def function_MotorPair():
    controll a pair of motors

    :param left_motor :  a sting as the left motor in the pair.
    :param right_motor : a sting a the right motor in the pair.
    :param speed : An integer as speed of the motor, from -100 to 100.
    :param angle : An integer as  angle of the motor, in degrees.

def function_ColoreSensor():
    Read the color of objects

    :param port : A sting form ("A","B","C","D","E","F") as the port wichi the motor is connected to on the hub.
    :param color : The  color is detected by the sensor.
    :param ambient_light_intensity : An ineteger as the  ambient light intensity detected by the sensor.
    :param reflected_light_intensity : An integer as  the  current reflected light intensity detected by the sensor.

def function_distanceSensor():
    Read the distance to the object

    :param port : A sting form ("A","B","C","D","E","F") as the port wichi the motor is connected to on the hub.


def function_Timer():
    Measure time




    >>>hub.speaker.beep()
    >>>start_hammer()
    >>>move_to_mid()
    >>>move_around_the_arena()



"""
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