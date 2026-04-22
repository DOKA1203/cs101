from cs1robots import *

create_world()
hubo = Robot(orientation='W', avenue=8, street=1)
hubo.set_trace("blue")
hubo.set_pause(0.01)

while not hubo.facing_north():
    hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()