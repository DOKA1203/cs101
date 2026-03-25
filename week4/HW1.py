from cs1robots import *
create_world()

turning_list = [8,17,26,34,42,49,56,62,68,73,78,82,86,89,92,94,96,97]

hubo = Robot(beepers=100)
hubo.set_trace("blue")
hubo.set_pause(0.01)
for i in range(99):
    hubo.drop_beeper()
    hubo.move()
    if i in turning_list:
        hubo.turn_left()

hubo.drop_beeper()