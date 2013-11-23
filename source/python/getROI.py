import numpy
import cv2
import pickle
import os

Win = False
if os.name == 'nt':
	Win = True

drawing = False
gx,gy = -1,-1
ROI = []

# mouse callback function
def draw_ROI(event,x,y,flags,param):
    global gx,gy,drawing,ROI

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        gx,gy = x,y
        cv2.line(imgBGR, (gx,gy), (x,y), (0,0,255), 2)

##    elif event == cv2.EVENT_MOUSEMOVE:       
##        if drawing == True:
##            cv2.rectangle(imgBGR,(gx,gy),(x,y),(0,255,0))
            

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(imgBGR,(gx,gy),(x,y),(0,0,255),2)
        ROI.append((gx,gy,x,y));
#check operating system
if Win:
	imgBGR = cv2.imread('..\..\data\empty1.jpg',1);
	origIMG = cv2.imread('..\..\data\empty1.jpg',1);
else:
	imgBGR = cv2.imread('../../data/empty1.jpg',1)
	origIMG = cv2.imread('../../data/empty1.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_ROI)

while(1):
    cv2.imshow('image', imgBGR)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
##for r in ROI:
##    (x1,y1,x2,y2) = r
##    cropped = origIMG[y1:y2,x1:x2, :]
##    cv2.imshow('image', cropped)
##    cv2.waitKey(0)
##cv2.destroyAllWindows()

f = open('ROIs1.txt', 'w')
pickle.dump(ROI, f);
f.close()





