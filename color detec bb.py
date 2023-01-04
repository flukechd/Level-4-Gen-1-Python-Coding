import cv2

# Start the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()

    # Convert the frame to the HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of red colors to detect
    lower_red = (136, 87, 111)
    upper_red = (180, 255, 255)
    # Define the range of Green colors to detect
    # lower_red = (25, 52, 72)
    # upper_red = (102, 255, 255)
    # Define the range of blue colors to detect
    # lower_red = (94, 80, 2)
    # upper_red = (120, 255, 255)

    # Create a mask for the frame using the lower and upper bounds of the red color
    mask = cv2.inRange(frame_hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a bounding box around the contour on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Show the result
    cv2.imshow("Result", frame)
    cv2.waitKey(1)
