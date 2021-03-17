import numpy as np
import cv2 

filename = input("Enter filename: ")  #輸入文件名
img = cv2.imread( filename, -1 )   #讀取圖像

nr, nc = img.shape[:2]  #shape屬性獲取圖像大小.(第一元素表示圖像的高度,第二表示圖像的寬度,第三表示像素的通道數)
print( "Number of Rows =", nr )  #行數
print( "Number of Columns =", nc)  #列數

if img.ndim != 3:
    print("Gray-Level Image") 
else: 
    print("Color Image")
