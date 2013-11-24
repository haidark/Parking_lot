import cv2
import sys

if len(sys.argv) < 2:
    print 'usage: save5frames.py <input video>'
    sys.exit(2)
    
video = cv2.VideoCapture(sys.argv[1])


for i in range(5):
    ret, img = video.read()
    file = 'f' + str(i+1) + '.jpg'
    cv2.imwrite(file, img)


print 'First 5 frames saved!'
