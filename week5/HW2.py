from cs1robots import *

load_world("../worlds/treasure.wld")
hubo = Robot(beepers=10)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def dance():
    for _ in range(5):
        hubo.turn_left()
        hubo.turn_left()
        hubo.turn_left()
        hubo.turn_left()

def move_nine():
    for _ in range(9):
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
            dance()

def zigzag():
    hubo.turn_left()
    move_nine()
    turn_right()
    hubo.move()
    turn_right()
    move_nine()

hubo.set_trace("blue")
hubo.set_pause(0.1)

for i in range(4):
    zigzag()
    hubo.turn_left()
    hubo.move()
zigzag()