# lab16-Image_Manipulation.py

from PIL import Image
import colorsys

img = Image.open('Lenna.png')
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #version one make it gray
        #y = 0.299*r + 0.587*g + 0.114*b
        #pixels[i, j] = (int(y), int(y), int(y))

#version two mess with hsv in photo
# colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h = h * 3
        s = s * .9
        v = v
# do some math on h, s, v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]
        pixels[i, j] = int(r*255), int(g*255), int(b*255)

img.show()
