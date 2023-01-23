import cv2
import numpy as np
def imreconstruct(img, marker):
    mask = img
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    recon1 = marker
    recon1_old = np.zeros(recon1.shape,np.int8)
    while np.sum(np.sum(recon1 - recon1_old)) != 0 :
        recon1_old = recon1;
        recon1 = cv2.dilate(recon1, se)
        #print(np.sum(np.sum(recon1 - recon1_old)))
        recon1 = recon1 & mask
    return recon1

# Load in Grayscale
img9 = cv2.imread('text_frombook.png')

# find the letter longer than one line
se = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 51))
img10 = cv2.erode(img9, se)

# reconstrction
img11 = imreconstruct(img9,img10)
cv2.imshow('long', img11)
# img12 =img9-img11
# cv2.imshow('long', img12)
cv2.waitKey(0)
cv2.destroyAllWindows()