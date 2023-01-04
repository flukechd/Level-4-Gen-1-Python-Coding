# Import the necessary libraries
import os
import cv2

# Set the directory containing the images
directory = "OutputImages"

# Loop through all files in the directory
for file in os.listdir(directory):
  # Read the image file
  img = cv2.imread(os.path.join(directory, file))

  # Convert the image to grayscale
  grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Convert the image to binary (black and white)
  _, binary_img = cv2.threshold(grayscale_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  # Show the grayscale and binary images together
  # Use cv2.hconcat to horizontally concatenate the images
  cv2.imshow("Grayscale and Binary Images", cv2.hconcat([grayscale_img, binary_img]))
  cv2.waitKey(0)
