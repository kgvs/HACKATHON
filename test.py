import numpy as np
import cv2


#cv2.resizeWindow('click', 600, 600)
img1 = cv2.imread('dog.png')
def mouseCoord(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        
        cv2.namedWindow('click', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('click',600,600)
        cv2.imshow('click', img1)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.imshow('base',base)
    if event == cv2.EVENT_LBUTTONUP:
        cv2.destroyWindow('click')

base = cv2.imread('black.png')


cv2.namedWindow('base', cv2.WINDOW_NORMAL)
cv2.resizeWindow('base', 600, 600)
cv2.imshow('base',base)
k = 0
    
cv2.setMouseCallback('base',mouseCoord)

cv2.waitKey(0)

