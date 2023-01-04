# QRCodeDetector From Webcam
import cv2
# create a VideoCapture object to read from the webcam
cap = cv2.VideoCapture(0)

# create a QR code detector
qr_code = cv2.QRCodeDetector()

while True:
    # read a frame from the webcam
    ret, frame = cap.read()

    # check if a frame was returned
    if not ret:
        break

    # find the QR code in the frame
    data, bbox, rectified_image = qr_code.detectAndDecode(frame)
    # display the edge-detected frame
    cv2.imshow('QRCodeDetector', frame)

    # check if the user pressed the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

    # check if a QR code was found
    if data:
        print("QR Code Data:", data)










    # QRCodeDetector From File
# import cv2
#
# # read the image
# image = cv2.imread("qr_code.png")
#
# # find the QR code in the image
# qr_code = cv2.QRCodeDetector()
# data, bbox, rectified_image = qr_code.detectAndDecode(image)
#
# # print the data
# print("QR Code Data:", data)