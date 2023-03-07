from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
timer = Timer()
# wait = wait()
# setting this motorpair to b and a means the robot moving backward is the new forward movement so we don't have to reverse all our values down below
movement_motors = MotorPair('A', 'B')
colour_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('D')
# lifting_arm = Motor('C')

# Write your program here.

# movement_motors.start()
# distance_sensor.wait_for_distance_closer_than(17, 'cm')
# movement_motors.stop()

# lifting_arm.run_to_position(270, 'shortest path', 10)
# lifting_arm.run_to_position(0, 'shortest path', 10)
# can replace shortest path with clockwise or counterclockwise
# if this doesn't work maybe try run_for_degrees instead of run_to_position

# steering equal to zero is going straight
# steering equal to +100 is going right
# steering equal to -100 is going left
# movement_motors.move(2, 'rotations', steering=0

#binary line following:

# while True:
#     if colour_sensor.get_color() == 'black':
#         movement_motors.start_tank(20, 0)
#     else:
#         movement_motors.start_tank(0, 20)

# proportional line following:
# find the halfway point between the reflective percentage for black and the reflective percentage for white, that should be steeering=0
# if the reflective light for black is 90 and the reflective light for white is 10, halfway point would be 45
# so when the reflective light is 45 that means it's likely on the edge of the black tape and white surface
movement_motors.set_default_speed(30)

# timer = 0
while True:
    # can add a multiplier for if the course designed has really sharp turn, if you multiply the number within the brackets it will cause the robot to correct itself with a sharper turn 
    movement_motors.start((colour_sensor.get_reflected_light() - 67)*2)
    light_value = colour_sensor.get_reflected_light()
    if colour_sensor.get_color() == 'green':
        movement_motors.stop()
        break
  
        # hub.light_matrix.write('timer =')
        # hub.light_matrix.write(timer.now())
    #     if timer.now() >= 2:
    #         # movement_motors.stop()
    #         # break
    # if colour_sensor.get_reflected light() < 80:
    #     timer.reset()

    # if colour_sensor.get_reflected light() > 80:
    #     timer = Timer()
    #     hub.light_matrix.write('timer =')
    #     hub.light_matrix.write(timer.now())
    #     if timer.now() >= 2:
    #         movement_motors.stop()
    #         in_motion = False
    # if colour_sensor.get_reflected light() < 80: