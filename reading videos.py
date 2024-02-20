import cv2 as cv

# if using webcam, use integer 0
capture = cv.VideoCapture('.idea/cat - Copy.mp4')

while True:
    # read video frame by frame, return boolean(success or not) and its frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

