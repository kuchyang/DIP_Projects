import numpy as np
import cv2

def image_quantization( f, bits ):
    g = f.copy()
    nr,nc = f.shape[:2]  #獲取圖像大小
    levels = 2 ** bits
    interval = 256 / levels  #間隔
    level_interval = 255 / (levels-1)
    table = np.zeros( 256 )
    for k in range(256):
        for l in range(levels):
            if k >= l*interval and l < (l+1)*interval:
                table[k] = round(l * level_interval)
    for x in range(nr):
        for y in range(nc):
            g[x,y] = np.uint8( table[f[x,y]] )
    return g

def main():
    filename = input("Enter filename: ")  #輸入文件名
    img1 = cv2.imread( filename, -1 )   #讀取圖像
    img2 = image_quantization( img1, 7 ) #位 7
    cv2.imshow( "original", img1 )  #顯示original圖像
    cv2.imshow( "quantization", img2 )  #顯示quantization圖像
    cv2.waitKey(0)
    
main()
