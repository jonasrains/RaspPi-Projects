import time
import math
from sense_emu import SenseHat
hat = SenseHat()
arrows = [False, False, False, False, False]

# colors
red = [255, 0, 0]
orange = [255, 127, 0]
yellow = [255, 255, 0]
lightGreen = [0, 255, 0]
green = [0, 150, 0]
blue = [0, 0, 255]
lightBlue = [0, 255, 255]
purple = [170, 0, 255]
pink = [255, 0, 255]
brown = [127, 64, 0]
white = [255, 255, 255]
black = [0, 0, 0]

# presets
def line(color, line, direction):
    # draws a verticle or horizontal line
    if direction == "horizontal":
        for i in range(64):
            if (line - 1) * 8 <= i < (line - 1) * 8 + 8:
                pixels[i] = color
    elif direction == "verticle":
        for i in range(8):
            for ii in range(1, 9):
                if ii == line:
                    pixels[i * 8 + ii - 1] = color

def fill(color):
    # use as pixels = fill()
    return([color for i in range(64)])

def pixel(color, x, y):
    for i in range(1, 9):
        for ii in range(1, 9):
            if i == y and ii == x:
                pixels[(i - 1) * 8 + ii-1] = color

def getPixel(x, y):
    for i in range(1, 9):
        for ii in range(1, 9):
            if i == y and ii == x:
                return(pixels[(i - 1) * 8 + ii-1])

def testPixel(x, y, color):
    if(getPixel(x, y) == color):
        return(True)
    else:
        return(False)

def mergeColor(color1, color2):
    return([round((color1[0] + color2[0]) / 2), round((color1[1] + color2[1]) / 2),
            round((color1[2] + color2[2]) / 2)])

def drawBG():
    line(black, 8, "horizontal")
    for i in range(4):
        pixel(black, i+5, 7)
    pixel(black, 1, 4)
    pixel(black, 1, 5)
    pixel(black, 2, 5)
    pixel(black, 3, 5)

# code
pixels = fill(black)
x = 1
y = 2
jumping = False
jumprep = 0
while True:
    for event in hat.stick.get_events():
        if event.direction == "up":
            if event.action == "held" or event.action == "pressed":
                arrows[0] = True
            else:
                arrows[0] = False
        if event.direction == "left":
            if event.action == "held" or event.action == "pressed":
                arrows[1] = True
            else:
                arrows[1] = False
        if event.direction == "right":
            if event.action == "held" or event.action == "pressed":
                arrows[2] = True
            else:
                arrows[2] = False
        if event.direction == "down":
            if event.action == "held" or event.action == "pressed":
                arrows[3] = True
            else:
                arrows[3] = False
        if event.direction == "middle":
            if event.action == "held" or event.action == "pressed":
                arrows[4] = True
            else:
                arrows[4] = False
    if arrows[0] and testPixel(x, y+1, black) and not jumping:
        jumping = True
        jumprep = 0
    if jumping:
        if not testPixel(x, y-1, black):
            jumprep += 1
            y -= 1
        else:
            jumprep = 0
            jumping = False
    if jumprep >= 5:
        jumping = False
        jumprep = 0
    if testPixel(x, y+1, black) and not jumping:
        y -= 1
    if arrows[1] or arrows[2]:
        if arrows[1]:
            if 1 < x:
                if not testPixel(x - 1, y + 1, black):
                    x -= 1
        if arrows[2]:
            if 8 > x:
                if not testPixel(x + 1, y + 1, black):
                    x += 1
    if not testPixel(x, y+1, black):
        if not jumping:
            y += 1
    pixels = fill(lightBlue)
    drawBG()
    pixel(blue, x, y)
    
    hat.set_pixels(pixels)
