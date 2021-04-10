import numpy as np
import cv2

def image_scale( img, Rotation, nr,nc):
    scale=0.5
    nrS=int(nr*scale)
    ncS=int(nc*scale)
    img2 = cv2.resize( img, (nrS,ncS), interpolation=cv2.INTER_LINEAR )
    return img2

def main():
    filename = input("Enter filename: ")  #輸入文件名
    img1 = cv2.imread(filename, -1 )   #讀取圖像lena.bmp
    nr2,nc2 = img1.shape[:2]
    Rotation = eval( input("Enter Rotation: ") )

    img2 = image_scale( img1, Rotation, nr2,nc2)
    rotation_matrix = cv2.getRotationMatrix2D( (nr2/2, nc2/2), Rotation, 1 )
    img3 = cv2.warpAffine( img2, rotation_matrix, (nr2, nc2) )
    

    cv2.imshow( "original", img1 )  #顯示original圖像
    cv2.imshow( "rotation_matrix", img3 )  #顯示圖像
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
