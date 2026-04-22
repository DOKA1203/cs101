from cs1media import *


threshold1 = 255 / 5
threshold2 = threshold1 * 2
threshold3 = threshold1 * 3
threshold4 = threshold1 * 4

img = load_picture("../image/a.png")
w, h = img.size()

for x in range(w):
    for y in range(h):
        r, g, b = img.get(x, y)

        v = (r + g + b) // 3

        if v < threshold1:
            img.set(x, y, (255, 255, 255))
        elif v < threshold2:
            img.set(x, y, (255, 0, 0))
        elif v < threshold3:
            img.set(x, y, (255, 255, 0))
        elif v < threshold4:
            img.set(x, y, (0, 0, 255))
        else:
            img.set(x, y, (0, 0, 0))

img.show()