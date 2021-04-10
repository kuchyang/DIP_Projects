import numpy as np
import cv2

filename = input("Enter filename: ")  #輸入文件名
img1 = cv2.imread(filename, -1 )   #讀取圖像
nr2,nc2 = img1.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D( (nr2/2, nc2/2), 30, 1 ) #參數(旋轉中心, 旋轉角度, 縮放比例)
rotation_matrix_1 = cv2.getRotationMatrix2D( (0, 0), 30, 1 ) #參數(旋轉中心, 旋轉角度, 縮放比例)
img2 = cv2.warpAffine( img1, rotation_matrix, (nr2, nc2) )
img3 = cv2.warpAffine( img1, rotation_matrix_1, (nr2, nc2) ) #參數(圖像, , 變換後的大小)

cv2.imshow( "original", img1 )  #顯示original圖像
cv2.imshow( "rotation_matrix", img2 )  #顯示圖像
cv2.imshow( "rotation_matrix_1", img3 )
cv2.waitKey(0)
cv2.destroyAllWindows()
