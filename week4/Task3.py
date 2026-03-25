from cs1robots import *


def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
def down_stair():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()


load_world("../worlds/newspaper.wld")

hubo = Robot(beepers=1)
hubo.set_trace("blue")
hubo.set_pause(0.01)

for _ in range(4):
    hubo.move()
    stair()

hubo.move()

hubo.drop_beeper()

hubo.turn_left()
hubo.turn_left()
for _ in range(4):
    hubo.move()
    down_stair()
hubo.move()