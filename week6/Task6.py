from cs1robots import *

m, n = (5,10)

create_world(avenues=n,streets=m)
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()


def round_trip():
    move_to_wall()
    turn_right()
    if hubo.front_is_clear():
        hubo.move()
        turn_right()
        move_to_wall()
        hubo.turn_left()
        if hubo.front_is_clear():
            hubo.move()
            hubo.turn_left()


if hubo.left_is_clear():
    hubo.turn_left()
    while hubo.front_is_clear():
        round_trip()
else:
    move_to_wall()