from cs1robots import *


def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

# create_world()

def move_around_wall():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()

load_world("../worlds/hurdles1.wld")

hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.set_pause(0.01)

hubo.move()
for _ in range(4):
    move_around_wall()
hubo.pick_beeper()