import cv2  
import numpy as np
img = cv2.imread('1.jpg')  
img = cv2.resize(img,(320,480),interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
canny=cv2.Canny(img,100,200)
_,contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),2)
cnt=contours[0]
print contours[0]
x, y, w, h = cv2.boundingRect(cnt)  #searching the outlines
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("canny", img)  
cv2.waitKey(0)