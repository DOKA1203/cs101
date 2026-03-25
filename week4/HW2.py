from cs1robots import *

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_five():
    for _ in range(5):
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()

def zigzag():
    hubo.pick_beeper()
    hubo.turn_left()
    move_five()
    turn_right()
    hubo.move()
    hubo.pick_beeper()
    turn_right()
    move_five()

load_world("../worlds/harvest4.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)

hubo.move()
zigzag()
hubo.turn_left()
hubo.move()
zigzag()
hubo.turn_left()

hubo.move()
zigzag()
hubo.turn_left()
