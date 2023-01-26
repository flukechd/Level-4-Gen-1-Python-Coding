import cv2

# Open the image
im = cv2.imread("shapes.png")

# Convert the image to grayscale
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image
threshold = 128
_, im_binary = cv2.threshold(im_gray, threshold, 255, cv2.THRESH_BINARY)

# Save the binary image
cv2.imshow('Webcam', im_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()