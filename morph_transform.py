import cv2 as cv
import numpy as np
img = cv.imread("C:/Users/ASUS/Desktop/j.png", cv.IMREAD_GRAYSCALE)
cv.imshow("image",img)
cv.waitKey(0)==ord('i')

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
cv.imshow("erosio",erosion)
cv.waitKey(0)==ord('e')

dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow("dilation",dilation)
cv.waitKey(0)==ord('d')

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow("opening",opening)
cv.waitKey(0)==ord('o')

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow("closing",closing)
cv.waitKey(0)==ord('c')

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow("gradient",gradient)      #best
cv.waitKey(0)==ord('g')

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow("tophat",tophat)
cv.waitKey(0)==ord('t')

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow("blackhat",blackhat)
cv.waitKey(0)==ord('b')