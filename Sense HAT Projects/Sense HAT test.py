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

def drawNumber(color, x, y, number):
    if number == 0:
        drawZero(color, x, y)
    elif number == 1:
        drawOne(color, x, y)
    elif number == 2:
        drawTwo(color, x, y)
    elif number == 3:
        drawThree(color, x, y)
    elif number == 4:
        drawFour(color, x, y)
    elif number == 5:
        drawFive(color, x, y)
    elif number == 6:
        drawSix(color, x, y)
    elif number == 7:
        drawSeven(color, x, y)
    elif number == 8:
        drawEight(color, x, y)
    elif number == 9:
        drawNine(color, x, y)
    else:
        drawNumber(color, x, y, int(str(number)[0]))
        drawNumber(color, x + 5, y, int(str(number)[1]))

def drawZero(color, x, y):
    pixel(color, x, y - 2)
    pixel(color, x - 1, y - 2)
    pixel(color, x - 1, y - 1)
    pixel(color, x - 1, y)
    pixel(color, x - 1, y + 1)
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y - 2)
    pixel(color, x + 1, y - 1)
    pixel(color, x + 1, y)
    pixel(color, x + 1, y + 1)
    pixel(color, x + 1, y + 2)

def drawOne(color, x, y):
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y + 2)
    pixel(color, x, y + 1)
    pixel(color, x, y)
    pixel(color, x, y - 1)
    pixel(color, x, y - 2)
    pixel(color, x - 1, y - 2)

def drawTwo(color, x, y):
    pixel(color, x - 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x + 1, y - 1)
    pixel(color, x + 1, y)
    pixel(color, x, y)
    pixel(color, x - 1, y + 1)
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y + 2)

def drawThree(color, x, y):
    pixel(color, x - 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x + 1, y - 1)
    pixel(color, x + 1, y)
    pixel(color, x, y)
    pixel(color, x + 1, y + 1)
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)

def drawFour(color, x, y):
    pixel(color, x - 1, y - 2)
    pixel(color, x + 1, y - 2)
    pixel(color, x - 1, y - 1)
    pixel(color, x + 1, y - 1)
    pixel(color, x - 1, y)
    pixel(color, x, y)
    pixel(color, x + 1, y)
    pixel(color, x + 1, y + 1)
    pixel(color, x + 1, y + 2)

def drawFive(color, x, y):
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y + 1)
    pixel(color, x - 1, y)
    pixel(color, x, y)
    pixel(color, x - 1, y - 1)
    pixel(color, x + 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x - 1, y - 2)

def drawSix(color, x, y):
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y + 1)
    pixel(color, x - 1, y)
    pixel(color, x, y)
    pixel(color, x - 1, y - 1)
    pixel(color, x + 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x - 1, y + 1)
    pixel(color, x + 1, y + 2)
    pixel(color, x + 1, y)

def drawSeven(color, x, y):
    pixel(color, x - 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x + 1, y - 2)
    pixel(color, x + 1, y - 1)
    pixel(color, x, y)
    pixel(color, x - 1, y + 1)
    pixel(color, x - 1, y + 2)

def drawEight(color, x, y):
    pixel(color, x, y - 2)
    pixel(color, x - 1, y - 1)
    pixel(color, x + 1, y - 1)
    pixel(color, x, y)
    pixel(color, x - 1, y + 1)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y + 1)

def drawNine(color, x, y):
    pixel(color, x + 1, y - 2)
    pixel(color, x, y - 2)
    pixel(color, x - 1, y - 1)
    pixel(color, x + 1, y)
    pixel(color, x, y)
    pixel(color, x + 1, y + 1)
    pixel(color, x - 1, y + 2)
    pixel(color, x, y + 2)
    pixel(color, x + 1, y - 1)
    pixel(color, x - 1, y - 2)
    pixel(color, x - 1, y)

def drawDigNumber(color, x, y, number):
    if number == 0:
        numList = [True, True, True, False, True, True, True]
    elif number == 1:
        numList = [False, False, False, False, False, True, True]
    elif number == 2:
        numList = [False, True, True, True, True, True, False]
    elif number == 3:
        numList = [False, False, True, True, True, True, True]
    elif number == 4:
        numList = [True, False, False, True, False, True, True]
    elif number == 5:
        numList = [True, False, True, True, True, False, True]
    elif number == 6:
        numList = [True, True, True, True, True, False, True]
    elif number == 7:
        numList = [False, False, True, False, False, True, True]
    elif number == 8:
        numList = [True for i in range(7)]
    elif number == 9:
        numList = [True, False, True, True, True, True, True]
    else:
        numList = [False for i in range(7)]
        drawDigNumber(color, x, y, int(str(number)[0]))
        drawDigNumber(color, x + 4, y, int(str(number)[1]))
    if numList[0]:
        pixel(color, x - 1, y - 2)
        pixel(color, x - 1, y - 1)
    if numList[1]:
        pixel(color, x - 1, y + 1)
        pixel(color, x - 1, y +2)
    if numList[2]:
        pixel(color, x, y - 3)
        pixel(color, x + 1, y - 3)
    if numList[3]:
        pixel(color, x, y)
        pixel(color, x + 1, y)
    if numList[4]:
        pixel(color, x, y + 3)
        pixel(color, x + 1, y + 3)
    if numList[5]:
        pixel(color, x + 2, y - 2)
        pixel(color, x + 2, y - 1)
    if numList[6]:
        pixel(color, x + 2, y + 1)
        pixel(color, x + 2, y + 2)

# code
pixels = fill(black)
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
                
    pixels = fill(lightBlue)
    
    hat.set_pixels(pixels)
