import numpy as np  #載入模組Numpy,命名空間改為np
import cv2  #載入模組opencv-python

img = cv2.imread("Lenna.bmp",-1)  #影像讀取
cv2.imshow("Example",img)  #影像顯示
cv2.waitKey(0)  #等待按鍵,才繼續執行。
cv2.destroyAllWindows()  #銷毀與釋放所有視窗
