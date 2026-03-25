from cs1robots import *


def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def left_top():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
def right_top():
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()


load_world("../worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)

for _ in range(5): hubo.move()
hubo.turn_left()
hubo.move()
for _ in range(5):
    hubo.pick_beeper()
    left_top()

for _ in range(5):
    hubo.pick_beeper()
    right_top()
hubo.turn_left()
hubo.turn_left()

for i in range(5, 0, -1):
    for _ in range(i):
        hubo.pick_beeper()
        left_top()
    for _ in range(i-1):
        hubo.pick_beeper()
        right_top()
    hubo.turn_left()
    hubo.turn_left()
hubo.pick_beeper()

