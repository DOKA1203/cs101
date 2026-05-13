from cs1graphics import *
from time import *

paper = Canvas()
ammo = 7

paper.setBackgroundColor('white')
paper.setWidth(800)
paper.setHeight(450)
paper.setTitle("Pistol")

pistol = Layer()

ammo_text = Text(f"AMMO ({ammo} / 7)", 20, Point(100, 20))
paper.add(ammo_text)

handgrip_x, handgrip_y = (300, 150)
hand_grip_height = 90
hand_grip_width = 40
giulgi = -10
hand_grip = Polygon(
    Point(handgrip_x + hand_grip_width, handgrip_y),
    Point(handgrip_x, handgrip_y),
    Point(handgrip_x + giulgi, handgrip_y + hand_grip_height),
    Point(handgrip_x + hand_grip_width + giulgi, handgrip_y + hand_grip_height))

hand_grip.setFillColor((100,100,100))
hand_grip.setDepth(10)
slide_x, slide_y = (360, 150)
slide_width = 150
slide_height = 24

slide_layer = Layer()
slide = Rectangle(slide_width, slide_height, Point(slide_x, slide_y))
slide.setFillColor('gray')
slide_hole = Rectangle(30, slide_height - 10, Point(slide_x-15, slide_y - 5))
slide_hole.setFillColor('black')
slide_layer.add(slide)
slide_layer.add(slide_hole)

slide_layer.setDepth(5)

pistol_body = Rectangle(slide_width, slide_height / 3, Point(slide_x, slide_y + slide_height / 2))
pistol_body.setFillColor((100,100,100))

pistol_body.setDepth(5)

barrel_x, barrel_y = (slide_x, slide_y)
barrel = Rectangle(slide_width / 2, slide_height / 2.5, Point(slide_x + 40, slide_y))
barrel.setFillColor('gold')
barrel.setDepth(10)

flaim = Circle(15, Point(slide_x + 98, slide_y))
flaim.setFillColor('white')
flaim.setBorderWidth(0)
flaim.setDepth(10)


paper.add(flaim)

empty_cartridge = Rectangle(20, 10, Point(slide_x - 20, slide_y))
empty_cartridge.setFillColor('gold')
empty_cartridge.setDepth(100)

paper.add(empty_cartridge)

def move_cartridge():
    for _ in range(20):
        sleep(0.1)
        empty_cartridge.move(-5, -5)
        empty_cartridge.rotate(-5)
    empty_cartridge.moveTo(slide_x - 20, slide_y)
    empty_cartridge.rotate(100)

pistol.add(barrel)
pistol.add(pistol_body)
pistol.add(slide_layer)
pistol.add(hand_grip)

magazine = Polygon(
    Point(handgrip_x + hand_grip_width - 10, handgrip_y),
    Point(handgrip_x, handgrip_y),
    Point(handgrip_x + giulgi, handgrip_y + hand_grip_height + 10),
    Point(handgrip_x + hand_grip_width + giulgi - 10, handgrip_y + hand_grip_height + 10))

magazine.setFillColor((100,100,100))
magazine.setDepth(1000)

trigger = Rectangle(30, 5, Point(handgrip_x + 45, handgrip_y+25))
trigger.rotate(45)
trigger.setFillColor('black')
trigger.setDepth(1000)

pistol.add(trigger)
pistol.add(magazine)
paper.add(pistol)

def bandong():
    pistol.rotate(-2)
    sleep(0.6)
    pistol.rotate(2)

def move_slide(direction):
    for _ in range(30):
        sleep(0.015)
        slide_layer.move(direction, 0)


def shoot():
    trigger.rotate(20)
    sleep(0.3)
    trigger.rotate(-20)

    global ammo
    ammo -= 1
    flaim.setFillColor('red')
    move_slide(-1)
    flaim.setFillColor('white')
    move_cartridge()
    bandong()
    ammo_text.setMessage(f"AMMO ({ammo} / 7)")
    if ammo == 0:
        return
    move_slide(1)



# animation
for i in range(2):
    sleep(1)
    for _ in range(7):
        shoot()
        sleep(1)

    for _ in range(150):
        magazine.move(0, 2)
        sleep(0.04)
    for _ in range(150):
        magazine.move(0, -2)
        sleep(0.04)

    ammo = 7
    ammo_text.setMessage(f"AMMO ({ammo} / 7)")

    sleep(2)

    move_slide(1)

ammo_text.setMessage(f"ENDDING")