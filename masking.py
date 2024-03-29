import cv2 as cv
import numpy as np

img = cv.imread('.idea/OIP.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (30, 30), (275, 700), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird shape masked image', masked)

cv.waitKey(0)