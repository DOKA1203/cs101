from cs1media import *

threshold1 = 255 / 3
threshold2 = threshold1 * 2


img = load_picture("../image/a.png")
w, h = img.size()

for x in range(w):
    for y in range(h):
        r, g, b = img.get(x, y)

        brightness = (r + g + b) // 3

        if brightness < threshold1:
            img.set(x, y, (0, 0, 255))
        elif brightness < threshold2:
            img.set(x, y, (0, 255, 0))
        else:
            img.set(x, y, (255, 255, 0))

img.show()