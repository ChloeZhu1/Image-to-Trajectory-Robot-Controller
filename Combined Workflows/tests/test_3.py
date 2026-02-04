import numpy as np
import cv2
import time
from multiprocessing import Process, Value, Array

cv2.namedWindow('frame')
def nothing(x):
    pass

def sync(n):
	fs="point.txt"
	fp=open(fs,"w")
	fp.write(str(n))
	fp.close()
	
global max,max_x,min,min_y
cap = cv2.VideoCapture(0)
#cv2.createTrackbar('Canny_L', 'frame', 300,300, nothing)
cv2.createTrackbar('Bin', 'frame', 90,255, nothing)
#cv2.createTrackbar('Canny_H', 'frame', 325,500, nothing)
while(True):
    # Capture frame-by-frame
	max=max_x=0
	
	ret, img = cap.read()
	num_rows, num_cols = img.shape[:2]
	rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -90, 1)
	img = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
	# L=cv2.getTrackbarPos('Canny_L', 'frame')
	# H=cv2.getTrackbarPos('Canny_H', 'frame')
	B=cv2.getTrackbarPos('Bin', 'frame')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, binary = cv2.threshold(gray,B,255,cv2.THRESH_BINARY_INV)
	#cv2.imshow('gray',gray)
	canny=cv2.Canny(binary,100,200)
	_,contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#cv2.drawContours(img,contours,-1,(0,0,255),2)
	for i in range(len(contours)):
		if len(contours[i])>80:
			cv2.drawContours(img,contours,i,(0,0,255),2)
			for k in range(len(contours[i])):
				if max<contours[i][k][0][1]<478:
					max=contours[i][k][0][1]
					max_x=contours[i][k][0][0]
				# if max<contours[i][k][0][0]<478:
					# max=contours[i][k][0][1]
					# max_x=contours[i][k][0][0]
	# cnt=contours[0]
	# print contours[0]
	# x, y, w, h = cv2.boundingRect(cnt)  #searching the outlines
	# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
	cv2.rectangle(img, (max_x, max), (max_x+50, max+50), (0, 255, 0), 2)
	sync(max)
	cv2.imshow('frame',img)
	#time.sleep(0.1)
	if cv2.waitKey(40) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()