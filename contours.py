import cv2 as cv
import numpy as np

img = cv.imread('.idea/pic.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Method 1: Find to the edges to get contours
canny = cv.Canny(img, 20, 120)
cv.imshow('Canny', canny)

# Method 2: Binaries the image using threshold to get contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
# RETR_TREE : all hierarchies contours
# RETR_EXTERNAL : external contours
# RETR_LIST : all contours in the image
# CHAIN_APPROX_SIMPLE
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# -1: draw all contours
cv.drawContours(blank, contours, -1,(0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)