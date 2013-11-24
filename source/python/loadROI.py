import numpy
import cv2
import pickle
import os
import sys

if len(sys.argv) < 4:
    print 'usage: loadROI.py <input ROI file> <empty lot image> <video file>'
    sys.exit(2);

#operating system flag
Win = False
if os.name == 'nt':
    Win = True

f = open(sys.argv[1], 'r');
ROI = pickle.load(f);
f.close();

origIMG = cv2.imread(sys.argv[2], 1);
video = cv2.VideoCapture(sys.argv[3])

#uncomment this line to capture video from available cameras
#video = cv2.VideoCapture(0)

templateEdges = [];
#Preload templates and precompute template edges
for r in ROI:
    (x1,y1,x2,y2) = r
    template = origIMG[y1:y2,x1:x2, :]
    template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    templateEdges.append(cv2.Canny(template, 100, 200))

#main loop
i = 0;
while True:
    #get the next frame
    ret, img = video.read()

    #we only want to look at every 120th frame
    if i % 120 == 0:
        #for every parking spot
        for spot in range(0,len(ROI)):
            (x1,y1,x2,y2) = ROI[spot]
            new = img[y1:y2,x1:x2, :]

            #convert to grayscale and extract Canny edges
            new = cv2.cvtColor(new, cv2.COLOR_RGB2GRAY)
            newEdges = cv2.Canny(new, 100, 200)

            #calculate the difference between template and new edges
            sub = cv2.absdiff(templateEdges[spot], newEdges)

            #normalize the difference normSub is array of 1's and zeros
            normSub = sub/255;

            threshPercent = 10;
            threshold = normSub.size*threshPercent/100;
            #print threshold
            #if there is greater than a 10% change between template and new edges
            #declare the parking spot occupied
            if sum(sum(normSub)) > threshold:
                if Win:
                    #draw a red rectangle to indicate an occupied spot
                    cv2.rectangle(img, (x1,y1), (x2,y2), [0, 0, 255], 2)
                else:
                    print 'Parking spot # ' + str(spot) + ': occupied'
            else:
                if Win:
                    #draw a green rectangle to indicate an unoccupied spot
                    cv2.rectangle(img, (x1,y1), (x2,y2), [0, 255, 0], 2)
                else:
                    print 'Parking spot # ' + str(spot) + ': occupied'
        if Win:
            #show the next frame in the image
            cv2.imshow('video', img)
        else:
            #clear the screen
            os.system('cls')

    if (0xFF & cv2.waitKey(5) == 27) | (ret == False):
        break

    i = i+1

if Win:
    cv2.destroyAllWindows()






