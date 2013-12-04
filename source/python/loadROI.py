import numpy
import cv2
import pickle
import os
import sys

if len(sys.argv) < 4:
    print 'usage: loadROI.py <input ROI file> <empty lot image> <video file>'
    sys.exit(2);

#operating system flag
#There are different modes of operation depending on OS.
Win = False
if os.name == 'nt':
    Win = True

#Read in ROIs from file
f = open(sys.argv[1], 'r');
ROI = pickle.load(f);
f.close();

#Read in image of empty parkinglot
origIMG = cv2.imread(sys.argv[2], 1);

#Read in video file to analyze
video = cv2.VideoCapture(sys.argv[3])

#uncomment this line to capture video from available cameras
#video = cv2.VideoCapture(0)


##uncomment these lines to output a video file.
#if Win:    
    #code to produce output video file
    #height , width , layers =  origIMG.shape
    #outvideo = cv2.VideoWriter(sys.argv[3][0:len(sys.argv[3])-4] + '_garbage.avi', -1, 3, (width, height));


templateEdges = [];
#Preload templates and precompute template edges

for r in ROI:
    (x1,y1,x2,y2) = r
    template = origIMG[y1:y2,x1:x2, :]
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

            #extract Canny edges
            newEdges = cv2.Canny(new, 100, 200)

            #calculate the difference between template and new edges
            sub = cv2.absdiff(templateEdges[spot], newEdges)

            #normalize the difference normSub is array of 1's and zeros
            normSub = sub/255;

            threshPercent = 10;
            threshold = normSub.size*threshPercent/100;

            #if there is greater than a 10% change between template and new edges
            #declare the parking spot occupied
            if sum(sum(normSub)) > threshold:
                if Win:
                    #draw a red rectangle to indicate an occupied spot
                    cv2.rectangle(img, (x1,y1), (x2,y2), [0, 0, 255], 2)
                    
                else:
                    #or print occupied
                    print 'Parking spot # ' + str(spot) + ': occupied'
            else:
                if Win:
                    #draw a green rectangle to indicate an unoccupied spot
                    cv2.rectangle(img, (x1,y1), (x2,y2), [0, 255, 0], 2)
                else:
                    #or print vacant
                    print 'Parking spot # ' + str(spot) + ': vacant'
        if Win:
            #show the next frame in the image
            cv2.imshow('video', img)
            cv2.imwrite('imageROIs.jpg', img);
            #outvideo.write(img)
        else:
            #clear the screen
            os.system('clear')

    if (0xFF & cv2.waitKey(5) == 27) | (ret == False):
        break

    i = i+1

if Win:
    cv2.destroyAllWindows()
    #outvideo.release()






