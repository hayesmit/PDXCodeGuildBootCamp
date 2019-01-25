# lab16-Image_Manipulation.py

from PIL import Image, ImageDraw
import colorsys
from random import randint
"""img = Image.open('Lenna.png')
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
"""


width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((250, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((250, 250, width-80, height-80), fill=color, width = 25)
draw.line((80, height - 80, 250, 250), fill=color, width=25)
draw.line((width/2, 100, width/2, 250), fill=color, width=25)
draw.line((100, 70, 250, 145), fill=color, width=25)
draw.line((width - 100, 70, 250, 145), fill=color, width=25)


circle_x = width/2
circle_y = 50
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()


#width = 500
#height = 500
#
#img = Image.new('RGB', (width, height))
#draw = ImageDraw.Draw(img)
#
#for i in range(1000):
#    x0 = randint(0, width)
#    y0 = randint(0, height)
#    x1 = randint(0, width)
#    y1 = randint(0, height)
#    line_width = randint(1, 40)
#    red = randint(0, 255)
#    green = randint(0, 255)
#    blue = randint(0, 255)
#    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)
#
#img.show()





















