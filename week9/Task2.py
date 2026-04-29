from cs1robots import *

load_world("../worlds/add34.wld")
hubo = Robot()
hubo.set_pause(0.1)

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

move_to_wall()
hubo.turn_left()

ollim = 0
while True:
    cnt = 0 + ollim
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
    hubo.move()

    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1

    turn_around()
    hubo.move()

    for i in range(cnt % 10):
        hubo.drop_beeper()
    ollim = cnt // 10

    turn_right()
    if cnt == 0:
        break
    hubo.move()
    turn_right()
