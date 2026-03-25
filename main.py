from cs1robots import *
# create_world()

load_world("worlds/add1.wld")

hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.set_pause(0.3)

hubo.move()

hubo.drop_beeper()

hubo.turn_left()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.turn_left()
hubo.move()
