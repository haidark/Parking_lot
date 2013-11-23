import numpy
import cv2
import pickle

def cls(): print "\n" * 100

f = open('ROIs1.txt', 'r');
ROI = pickle.load(f);
f.close();
origIMG = cv2.imread('C:\Users\Haidar\Documents\GitHub\N02062147\data\empty1.jpg',1);
templateEdges = [];
#Pre load and precompute templates and template edges
for r in ROI:
    (x1,y1,x2,y2) = r
    template = origIMG[y1:y2,x1:x2, :]
    template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    templateEdges.append(cv2.Canny(template, 100, 200))



video = cv2.VideoCapture('C:\Users\Haidar\Documents\GitHub\N02062147\data\carParkFootage.mp4')
#video = cv2.VideoCapture(0)
i = 0;
while True:
    
    ret, img = video.read()
    if i % 120 == 0:
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

            threshPercent = 5;
            threshold = normSub.size*threshPercent/100;
            #print threshold
            #if there is greater than a 10% change between template and new edges
            #declare the parking spot occupied
            if sum(sum(normSub)) > threshold:
                #draw a red rectangle to indicate an occupied spot
                cv2.rectangle(img, (x1,y1), (x2,y2), [0, 0, 255], 2)
            else:
                #draw a green rectangle to indicate an unoccupied spot
                cv2.rectangle(img, (x1,y1), (x2,y2), [0, 255, 0], 2)
        #show the next frame in the image
        cv2.imshow('video', img)
    if (0xFF & cv2.waitKey(5) == 27) | (ret == False):
            break    
    i = i+1

cv2.destroyAllWindows()






