from cs1media import *




img = load_picture("../image/geowi.jpg")
w, h = img.size()

for x in range(w):
    for y in range(h):
        if not w//5 < x < w-w//5 or not h//5 < y < h-h//5:
            r, g, b = img.get(x, y)
            img.set(x, y, (255 - r,255- g,255- b))

img.show()