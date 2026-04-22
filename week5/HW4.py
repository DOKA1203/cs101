from cs1robots import *

create_world()

hubo1 = Robot(beepers=12)
hubo1.set_trace("blue")
hubo1.set_pause(0.01)

hubo2 = Robot()
hubo2.set_trace("red")
hubo2.set_pause(0.01)

turn_count = 0

hubo1.move()

while turn_count != 4 * 3:
    if not hubo1.front_is_clear():
        turn_count += 1
        hubo1.drop_beeper()
        hubo1.turn_left()
    if not hubo2.front_is_clear():
        hubo2.pick_beeper()
        hubo2.turn_left()
    hubo1.move()
    hubo2.move()

hubo2.pick_beeper()

for _ in range(12): # DANCE
    hubo2.turn_left()