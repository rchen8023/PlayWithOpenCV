import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg") # defalt as color image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces return a numpy array with 4 values,
# [[row of detected face start point, column of detected face start point, face width, face height]]
faces = face_cascade.detectMultiScale(gray_img, 
                        scaleFactor=1.05,
                        minNeighbors=5)

for x, y, w, h in faces:
    # create rectangle of detected face
    # x, y are the starting point of the rectangle (top left)
    # x+w, y+h are the bottom right point of the rectangle
    # (0,255,0) is the color of rectangle (B,G,R)
    # 3 is the thickness of rectangle
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()