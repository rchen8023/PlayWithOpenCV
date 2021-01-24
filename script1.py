import cv2

img = cv2.imread("galaxy.jpg",0) # pass 1 for RBG image, 0 for gray scale, -1 for color image with transparency
# the type of img is a numpy array, 2-d array for gray scale, 3-d array for RBG
# numpy.shape = (rows, columns)
# cv2.resize(image,(columns, rows))
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # resize the image. 
cv2.imshow("Galaxy",img) # display the image in a new window
cv2.imwrite("Galaxy_resized.jpg",resized_img) # create a new image. 
cv2.waitKey(0) # make the window stay for some time, 0 - when user press any button, others in mseconds
cv2.destroyAllWindows()