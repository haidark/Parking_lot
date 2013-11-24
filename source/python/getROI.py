import numpy
import cv2
import pickle
import os
import sys

if len(sys.argv) < 3:
    print 'usage: getROI.py <empty lot image> <output ROI filename>'
    sys.exit(2)

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
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(imgBGR,(gx,gy),(x,y),(0,0,255),2)
        ROI.append((gx,gy,x,y));

#load image
imgBGR = cv2.imread(sys.argv[1],1);
origIMG = cv2.imread(sys.argv[1],1);

#create window and point to mouse callback
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_ROI)

#main loop
while(1):
    #show the image
    cv2.imshow('image', imgBGR)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

#write data to output file
f = open(sys.argv[2], 'w')
pickle.dump(ROI, f);
f.close()





