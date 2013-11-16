import numpy
import cv2
import pickle

f = open('ROIs.txt', 'r');
ROI = pickle.load(f);
f.close();
origIMG = cv2.imread('C:\Users\Haidar\Documents\GitHub\N02062147\data\empty1.jpg',1);



video = cv2.VideoCapture('C:\Users\Haidar\Documents\GitHub\N02062147\data\carParkFootage.mp4')
#video = cv2.VideoCapture(0)
i = 0;
while True:
    ret, img = video.read()
    if i % 120 == 0: 
        r = ROI[5]
        (x1,y1,x2,y2) = r
        template = origIMG[y1:y2,x1:x2, :]
        new = img[y1:y2,x1:x2, :]
        #convert to grayscale
        template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
        new = cv2.cvtColor(new, cv2.COLOR_RGB2GRAY)
        sub = cv2.absdiff(template, new)
        normSub = sub/255.0;
        if sum(sum(normSub)) > 1500:
            print 'slot 6 : occupied'
        else:
            print 'slot 6 : vacant'
    
        cv2.imshow('some', sub)
        if (0xFF & cv2.waitKey(5) == 27) | (ret == False):
            break
    i=i+1
cv2.destroyAllWindows()






