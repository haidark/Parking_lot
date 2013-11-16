import cv2
video = cv2.VideoCapture('C:\Users\Haidar\Documents\GitHub\N02062147\data\carParkFootage.mp4')
#video = cv2.VideoCapture(0)
i = 1;
while True:
    ret, img = video.read()
    if i < 6:
        file = 'C:\Users\Haidar\Documents\GitHub\N02062147\data\carParkFootage\f' + str(i) + '.jpg'
        cv2.imwrite(file, img)
    i = i + 1
    cv2.imshow('some', img)
    if (0xFF & cv2.waitKey(5) == 27) | (ret == False):
        break
cv2.destroyAllWindows()
