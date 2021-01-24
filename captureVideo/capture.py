import cv2, time

# capture video from web camera
# cv2.VideoCapture(...) the parameter can be the index of number of cameras, or the video file (ex: .mp4)
video = cv2.VideoCapture(0)

while True:
    # check returns boolean variable whether the video is running or not
    # frame returns a numpy array 3-d if colored video
    check, frame = video.read()

    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # change video to gray scale 

    #time.sleep(3)
    cv2.imshow("Capturing",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break 

video.release()
cv2.destroyAllWindows()