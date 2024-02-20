import cv2 as cv

img = cv.imread('.idea/OIP.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
# thresh: threshold image, binarize image
# threshold: the thresh value I pass
threshold, thresh = cv.threshold(gray, 170, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
cv.waitKey(0)