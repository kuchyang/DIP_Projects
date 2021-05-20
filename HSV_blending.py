import cv2

img,im = cv2.imread( "Jenny.bmp", -1 ), cv2.imread("Baboon.bmp",-1)
hsv,hsv2 = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ),cv2.cvtColor( im, cv2.COLOR_BGR2HSV )
h, s, v = cv2.split(hsv) 
h2, s2, v2 = cv2.split(hsv2) 

hsv = cv2.merge([h2, s, v]) 
out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) 
cv2.imshow("ex", out) 
cv2.waitKey() 
