from cs1robots import *

load_world("../worlds/harvest3.wld")

hubo = Robot(beepers=100)
hubo.set_trace("blue")
hubo.set_pause(0.01)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_five():
    for _ in range(5):
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()

hubo.move()

for i in range(3):
    move_five()
    hubo.turn_left()
    hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()
    hubo.turn_left()
    move_five()
    if i != 2:
        turn_right()
        hubo.move()
        if not hubo.on_beeper():
            hubo.drop_beeper()
        turn_right()