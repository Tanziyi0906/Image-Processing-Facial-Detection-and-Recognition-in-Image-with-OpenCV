import cv2 as cv

img = cv.imread('.idea/OIP.jpg')

# this is BGR image (3 channel) #
cv.imshow('Car', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 30, 80)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny,(7, 7), iterations=3)
cv.imshow('Dilate', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Erode', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[500:900, 300:600]
cv.imshow('Cropped', cropped)
cv.waitKey(0)