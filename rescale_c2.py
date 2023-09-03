import cv2 as cv

# Modify width and height of frame by scale then pack into a tuple and return resized frame
# This method works for images, videos and live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# This method only works for live videos
def changeRes(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

def videoRead():
    capture = cv.VideoCapture("videos/dog1.mp4")
    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            break
        frame_resized = rescaleFrame(frame)
        cv.imshow("Dog - normal", frame) # Normal frame
        cv.imshow("Dog - resized", frame_resized) # Rescaled frame
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    capture.release()
    cv.destroyAllWindows()

def imageRead():
    img = cv.imread("photos/cat2.jpg")
    img_resized = rescaleFrame(img, 0.35)
    cv.imshow("Cat - normal", img)
    cv.imshow("Cat - resized", img_resized)
    cv.waitKey(0)

def liveStream():
    capture = cv.VideoCapture(0)
    changeRes(capture, 100, 100)
    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            break
        cv.imshow("Live preview", frame)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    capture.release()
    cv.destroyAllWindows()