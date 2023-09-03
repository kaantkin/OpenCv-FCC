# Read images and videos with OpenCV #
import cv2 as cv

def readImage():
    img = cv.imread("photos/cat1.jpg") # Takes in path of image and returns pixels of image in matrix

    cv.imshow("Cat", img) # Display image in new window. Takes in the name of window and matrix of pixels to display

    cv.waitKey(0) # Waits a specific time for a key to be pressed. 0 means infinite.


def readVideo():
    capture = cv.VideoCapture("videos/dog1.mp4") # Takes in either a path of video, or an integer which represents the input device connected (eg camera)

    # Loop used to read video frame by frame
    while True:
        isTrue, frame = capture.read() # read() returns a boolean stating if successfully read and each frame of the video

        # If no more frames (ie, video ended) or frame cant be read then end
        if not isTrue:
            break

        cv.imshow("Dog", frame)

        # close video when D key pressed
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
        
    
    # Cleanup
    capture.release() # release capture pointer
    cv.destroyAllWindows()


readVideo()