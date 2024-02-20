import cv2 as cv


def rescaleFrame(frame, scale):
    # can use in image, video, live #
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# take the path to the image and return the image as pixels#
img = cv.imread('.idea/OIP.jpg')

resized_image = rescaleFrame(img, 0.5)

# display into window #
cv.imshow('Cat', img)

cv.imshow('Cat_resized', resized_image)

# if using webcam, use integer 0
capture = cv.VideoCapture('.idea/cat - Copy.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 3.75)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()