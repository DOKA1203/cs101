from cs1robots import *

load_world("../worlds/hurdles3.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def hurdle():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()


flag = False

while True:
    while hubo.front_is_clear():
        if hubo.on_beeper():
            hubo.pick_beeper()
            flag = True
            break
        hubo.move()
    if not flag:
        if hubo.on_beeper():
            hubo.pick_beeper()
            flag = True
            break
        hurdle()
    else:
        break
