import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # Create a blank canvas - .zeros() returns a new array of a given shape and type filled with zeros
cv.imshow("Blank Canvas", blank)

# 1. Paint image a certain color
def paintColor():
    blank[:] = 0,255,0 # Reference all pixels and set to green value
    # blank[200:300, 300:400] = 0,255,0 - Colors specific point on canvas
    cv.imshow("Green", blank)

# 2. Draw a rectangle
def drawRect():
    cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # Draw a rectangle on blank from start point 0,0 to end point 250,250 (which is the half-way point)
    # cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) - Shape is half of original canvas size
    cv.imshow('Rectangle', blank)

# 3. Draw a circle
def drawCircle():
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
    cv.imshow('Circle', blank)

# 4. Draw a line
def drawLine():
    cv.line(blank, (0,0), (250,250), (0,255,0), thickness=2)
    cv.imshow("Line", blank)

# 5. Write text
def writeText():
    cv.putText(blank, "Hello World", (0, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
    cv.imshow("Text", blank)

writeText()

cv.waitKey(0)