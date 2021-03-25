import numpy as np
import cv2

def image_downsampling( f, sampling_rate ):
    nr,nc = f.shape[:2]  #獲取圖像大小
    nr_s = nr//sampling_rate
    nc_s = nc//sampling_rate
    g2= np.zeros( [nr,nc,3], dtype='uint8' )
    for x in range(nr_s):
        for y in range(nc_s):
            g2[x*sampling_rate,y*sampling_rate]=f[x,y]
            g2[x*sampling_rate,y*sampling_rate+1]=f[x,y]
            g2[x*sampling_rate+1,y*sampling_rate]=f[x,y]
            g2[x*sampling_rate+1,y*sampling_rate+1]=f[x,y]
    return g2
  
def main():
    filename = input("Enter filename: ")  #輸入文件名
    img1 = cv2.imread(filename, -1 )   #讀取圖像
    img2 = image_downsampling( img1, 2 ) #採樣率 2
    cv2.imshow( "original", img1 )  #顯示original圖像
    cv2.imshow( "Upsampling", img2 )  #顯示image formation model圖像
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()
