import numpy as np
import cv2

def image_formation_model( f, x0, y0, sigma ):
    g = f.copy()
    nr, nc = f.shape[:2]  #獲取圖像大小
    illumination = np.zeros( [nr,nc], dtype='fioat32' )
    
    return g
  
def main():
    filename = input("Enter filename: ")  #輸入文件名
    img = cv2.imread( filename, -1 )   #讀取圖像
    nr, nc = img.shape[:2]  #獲取圖像大小
    x0 = nr // 2
    y0 = nc // 2
    sigma = 400 #1600
    img2 = image_formation_model( img, x0, y0, sigma )
    cv2.imshow( "original", img )  #顯示original圖像
    cv2.imshow( "image formation model", img2 )  #顯示image formation model圖像
    cv2.waitKey(0)
    
main()
