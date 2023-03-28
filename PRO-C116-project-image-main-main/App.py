import cv2 
image = cv2.imread("solar-system.jpg")

cv2.putText(image, "Sun" , (50,50) , cv2.FONT_HERSHEY_COMPLEX  , 2 , (225, 0 , 0) , 2 )
cv2.putText(image, "Mercury" , (120,200) , cv2.FONT_HERSHEY_COMPLEX  , .6 , (225, 0 , 0) , 2 )
cv2.putText(image, " Venus" , (165 , 230) , cv2.FONT_HERSHEY_COMPLEX  , .6 , (225, 0 , 0) , 2 )
cv2.putText(image, " Earth " , (270 , 270) , cv2.FONT_HERSHEY_COMPLEX  , .6 , (225, 0 , 0) , 2 )

cv2.imshow("solarsystem" , image)
cv2.waitKey(3000)
