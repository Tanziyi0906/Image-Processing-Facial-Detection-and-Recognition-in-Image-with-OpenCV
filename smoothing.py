import cv2 as cv

img = cv.imread('.idea/OIP.jpg')
cv.imshow('Cats', img)

# Averaging
averaging = cv.blur(img, (3, 3))
cv.imshow('Average Blur', averaging)

# Gaussian Blur (certain weight value applied when compute the blur)
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median blur (more effective in reducing noise)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral (retain edges of image) (larger sigma color, more neighbourhood color will be considered)
# large sigma space, pixels further around from central sigma will influence the blurring calculation
bilateral = cv.bilateralFilter(img, 10, 30, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)