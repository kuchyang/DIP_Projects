import numpy as np
import cv2 

filename = input( "Please enter filename: " )  #請輸入文件名
img = cv2.imread( filename, -1 ) 
nr, nc = img.shape[:2] 
print( "Number of Rows =", nr ) 
print( "Number of Columns =", nc) 
if img.ndim != 3:
  print( "Gray-Level Image") 
else: 
  print( "Color Image")
