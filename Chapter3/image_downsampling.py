import numpy as np
import cv2

def image_downsampling( f, sampling_rate ):
    nr,nc = f.shape[:2]  #獲取圖像大小
    nr_s,nc_s = nr//sampling_rate, nc//sampling_rate
    g = np.zeros( [nr_s,nc_s], dtype='uint8' )
    for x in range(nr_s):
        for y in range(nc_s):
            g[x,y] = f[x*sampling_rate, y*sampling_rate]
    return g

def main():
    filename = input("Enter filename: ")  #輸入文件名
    img1 = cv2.imread( filename, -1 )   #讀取圖像
    img2 = image_downsampling( img1, 2 ) #採樣率 2
    cv2.imshow( "original", img1 )  #顯示original圖像
    cv2.imshow( "downsampling", img2 )  #顯示image formation model圖像
    cv2.waitKey(0)
    
main()
