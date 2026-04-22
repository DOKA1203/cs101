from cs1robots import *

load_world("../worlds/trash2.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

while hubo.front_is_clear():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()
hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
turn_right()
hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()
hubo.turn_left()
hubo.turn_left()
hubo.move()
hubo.turn_left()