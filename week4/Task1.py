from cs1robots import *

create_world()
hubo = Robot(beepers=10)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_nine():
    for _ in range(9):
        hubo.move()

def zigzag():
    hubo.turn_left()
    move_nine()
    turn_right()
    hubo.move()
    turn_right()
    move_nine()

hubo.set_trace("blue")
hubo.set_pause(0.01)

for i in range(4):
    zigzag()
    hubo.turn_left()
    hubo.move()
zigzag()