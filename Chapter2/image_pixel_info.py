import numpy as np
import cv2

global img  #全域變數

def onMouse( event, x, y, flags, param ):
    x,y = y,x  #cv2的[軸]定義與數位影像相反,因此要交換
    if img.ndim != 3:
        print( "(x,y) = (%d,%d)" %(x,y), end = "  " )
        print( "Gray-Level = %3d" %img[x,y] )
    else:
        print( "(x,y) = (%d,%d)" %(x,y), end = "  " )
        print( "(R,G,B) = (%3d,%3d,%3d)" %(img[x,y,2],img[x,y,1],img[x,y,0]) )  #cv2存取順序式(B,G,R)

filename = input( "Please enter filename:" )
img = cv2.imread( filename,-1 )
cv2.namedWindow( filename )  #建新視窗
cv2.setMouseCallback( filename, onMouse )  #回呼(Callback)函式:滑鼠觸發事件(event),呼叫副函式(onMouse)
cv2.imshow( filename,img )  #顯示圖像
cv2.waitKey(0)
