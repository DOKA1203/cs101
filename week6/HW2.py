from cs1robots import *

load_world("../worlds/6w_2.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def collect():
    while hubo.front_is_clear():
        if hubo.on_beeper():
            hubo.pick_beeper()
        hubo.move()
        if not hubo.on_beeper():
            break
    if hubo.on_beeper():
        hubo.pick_beeper()

for i in range(3):
    collect()
    hubo.turn_left()
    while not hubo.on_beeper():
        hubo.move()
    turn_right()
collect()
hubo.turn_left()
collect()

print("I did it")

