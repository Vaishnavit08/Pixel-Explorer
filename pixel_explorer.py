# aim: create a function which help to find coordinate of any pixel and its color
# left click= color's GBR value
# right click = co-ordinate values


import cv2
import numpy as np

def Find_cor(event,x,y,flag,param):
    font=cv2.FONT_ITALIC

    if event== cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ', y)

        cord= '. '+str(x) +' , '+str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        # cv2.imshow('image',img)

    if event== cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]  # for blue chanel 0
        g=img[y,x,1]  # for green channel is 1
        r=img[y,x,2]  # for red channel is 2

        color_bgr=" . " + str(b) + ", "+ str(g)+ ", "+ str(r)

        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        # cv2.imshow('images',img)

cv2.namedWindow(winname='res')

img=np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback('res',Find_cor)

while True:
        cv2.imshow('res',img)

        k=cv2.waitKey(1)=='v'
        if k==ord('v'):
             break
        
cv2.destroyAllWindows()

