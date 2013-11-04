import numpy
import cv2

imgBGR = cv2.imread('stop.jpg',1);
cv2.imshow('image', imgBGR)

cv2.destroyAllWindows()

imgHSV = cv2.cvtColor(imgBGR,cv2.COLOR_RGB2HSV)

cv2.imshow('image', imgHSV)

cv2.destroyAllWindows()

H,S,V = cv2.split(imgHSV)
hLow = 0;
hHigh = 360;
sLow = 0;
sHigh = 100;
vLow = 0;
vHigh = 100;

cv2.imshow('image', V)
#cv2.waitKey(0)
cv2.destroyAllWindows()
H = numpy.array(H);
print H
if hLow <= hHigh:
    hRange = H >= hLow & H <= hHigh;
else:
    hRange = H <= hHigh | H >= hLow;
