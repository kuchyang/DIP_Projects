import numpy as np
import cv2

def image_scale( Degree, nr,nc):
    Rad = Degree * np.pi / 180
    scale = np.sin(Rad) 
    #scale45=np.sin(45 * np.pi / 180)
    #print(scale)
    Deg1=Degree%90
    if Deg1 == 0:
        size = 1
    elif Deg1 > 45:
        #p=pow(np.sin(Rad),2)+pow(np.cos(Rad),2)
        #np.sqrt(p)
        size = np.sin(45 * np.pi / 180)
    elif Deg1 < 45:
        size = np.cos(45 * np.pi / 180) #1-(1-scale45)*(Deg1)/45
        #print(size)
    else :
        size = scale
    return size

def main():
    #filename = input("Enter filename: ")  #輸入文件名
    img1 = cv2.imread("lena.bmp", -1 )   #讀取圖像lena.bmp
    nr2,nc2 = img1.shape[:2]
    Rotation = eval( input("Enter Rotation: ") )
    Scale = image_scale( Rotation, nr2,nc2) #0.7

    rotation_matrix = cv2.getRotationMatrix2D( (nr2/2, nc2/2), Rotation, Scale )
    img2 = cv2.warpAffine( img1, rotation_matrix, (nr2, nc2) )

    cv2.imshow( "original", img1 )  #顯示original圖像
    cv2.imshow( "rotation_matrix", img2 )  #顯示圖像
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
