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
    motor_pair.move_tank(0.15, 'rotations', 10, 10)
    claw_motor.run_to_position(130, 'shortest path', 30)


hub.speaker.beep()
claw_motor.run_to_position(355, 'shortest path', 30)
claw_motor.run_to_position(130, 'shortest path', 30)
claw_motor.run_to_position(355, 'shortest path', 30)
motor_pair.move_tank(0.25, 'rotations', 70, 70)
# main_loop_count = 0
rotation_count = 0.25

while claw_motor.get_position() > 200:
    while color_sensor.get_reflected_light() > 80 and claw_motor.get_position() > 200:
        motor_pair.move_tank(0.25, 'rotations', 50, 50)
        rotation_count += 0.25
        if distance_sensor.get_distance_cm() in range(6):
            ball_pickup()

    while rotation_count > 0.25:
        motor_pair.move_tank(-0.25, 'rotations', 50, 50)
        rotation_count -= 0.25

    motor_pair.move_tank(0.125, 'rotations', 25, -25)