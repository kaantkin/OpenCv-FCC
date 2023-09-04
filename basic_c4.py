import cv2 as cv

img = cv.imread("photos/cat2.jpg")

def grayscale():
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale", grey)

def blurImg():
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    cv.imshow("Blur", blur)

# Edge cascade, find how many edges are present in the image
def edgeCascadeCanny():
    canny = cv.Canny(img, 125, 175) # To reduce the amount of edges you can pass in a blurred image to Canny
    cv.imshow("Canny Edges", canny)

# Dilating image
def dilate():
    canny = cv.Canny(img, 125, 175) # From prev example
    dilated = cv.dilate(canny, (3,3), iterations=1)
    cv.imshow("Dilated", dilated)

# Eroding image
def erode():
    canny = cv.Canny(img, 125, 175) # From prev example
    eroded = cv.erode(canny, (3,3), iterations=1)
    cv.imshow("Eroded", eroded)

# Cropping
def crop():
    cropped = img[0:200, 200:400]
    cv.imshow("Crop", cropped)

crop()

cv.waitKey(0)