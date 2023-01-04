import cv2
import numpy as np

# create a video capture object to read frames from the webcam
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the webcam
    _, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply the Sobel operator to find the horizontal and vertical edges
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # combine the results to get the final image
    edges = np.hypot(sobel_x, sobel_y)
    edges = edges / edges.max() * 255
    edges = np.uint8(edges)

    # display the edge-detected frame
    cv2.imshow('Edge Detection', edges)

    # check if the user pressed the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# release the video capture object
cap.release()
