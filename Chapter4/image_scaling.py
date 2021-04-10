import numpy as np
import cv2

filename = input("Enter filename: ")  #輸入文件名
img1 = cv2.imread(filename, -1 )   #讀取圖像
nr,nc = img1.shape[:2]

scale = eval( input("Enter scale: ") )
nr2=int(nr*scale)
nc2=int(nc*scale)
img2 = cv2.resize( img1, (nr2,nc2), interpolation=cv2.INTER_LINEAR) #

cv2.imshow( "original", img1 )  #顯示original圖像
cv2.imshow( "scaling", img2 )  #顯示scaling圖像
cv2.waitKey(0)
cv2.destroyAllWindows()
