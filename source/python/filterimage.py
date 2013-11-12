import numpy
import cv2

imgBGR = cv2.imread('stop.jpg',1);
cv2.imshow('image', imgBGR)

cv2.destroyAllWindows()

imgHSV = cv2.cvtColor(imgBGR,cv2.COLOR_RGB2HSV)

cv2.imshow('image', imgHSV)

cv2.destroyAllWindows()

H,S,V = cv2.split(imgHSV)
hLow = 345;
hHigh = 15;
sLow = 0;
sHigh = 100;
vLow = 0;
vHigh = 100;

print H.shape[1]
#Initialize logical matrices for  ranges and final filtered image
hRange = numpy.zeros(H.shape)
sRange = numpy.zeros(S.shape)
vRange = numpy.zeros(V.shape)
filtered = numpy.zeros(H.shape)

##cv2.imshow('image', V)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

if hLow <= hHigh:
    for i in xrange(H.shape[0]):
        for j in xrange(H.shape[1]):
            hRange[i,j] = H[i,j] >= hLow & H[i,j] <= hHigh;
    
else:
    for i in xrange(H.shape[0]):
        for j in xrange(H.shape[1]):
            hRange[i,j] = H[i,j] >= hLow & H[i,j] <= hHigh;

if sLow <= sHigh:
    for i in xrange(S.shape[0]):
        for j in xrange(S.shape[1]):
            sRange[i,j] = S[i,j] >= sLow & S[i,j] <= sHigh;
    
else:
    for i in xrange(S.shape[0]):
        for j in xrange(S.shape[1]):
            sRange[i,j] = S[i,j] >= sLow & S[i,j] <= sHigh;
