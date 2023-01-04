import cv2
import os

# create a video capture object to read frames from the webcam
cap = cv2.VideoCapture(0)

# specify the number of images to capture
num_images = 10

# create the OutputImages folder if it does not exist
if not os.path.exists('OutputImages'):
    os.makedirs('OutputImages')

# capture and save the specified number of images
for i in range(num_images):
    while True:
        # read a frame from the webcam
        _, frame = cap.read()

        # display the frame
        cv2.imshow('Webcam', frame)

        # check if the user pressed the 'c' key
        if cv2.waitKey(1) == ord('c'):
            # save the frame to an image file in the OutputImages folder
            cv2.imwrite('OutputImages/image{}.jpg'.format(i), frame)
            break

# release the video capture object
cap.release()
