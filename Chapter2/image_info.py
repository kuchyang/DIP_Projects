import numpy as np
import cv2 

filename = input( "Enter filename: " )  #輸入文件名
img = cv2.imread( filename, -1 ) 

nr, nc = img.shape[:2] 
print( "Number of Rows =", nr )  #行數
print( "Number of Columns =", nc)  #列數

if img.ndim != 3:
  print("Gray-Level Image") 
else: 
  print("Color Image")
