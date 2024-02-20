import cv2 as cv


# take the path to the image and return the image as pixels#
img = cv.imread('.idea/OIP.jpg')

# display into window #
cv.imshow('Cat', img)

# keyboard binding function
cv.waitKey(0)