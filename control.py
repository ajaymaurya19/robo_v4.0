import cv2
import numpy as np
#from robo_AI import setServoAngle

from robo_move3 import angle
cap = cv2.VideoCapture(0)

cap.set(3,640.0) #set the size
cap.set(4,480.0)

angle(120, 70)
face_classifier = cv2.CascadeClassifier('/media/password/nvidia/Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml')
rows = 480
cols = 640
x_medium = int(cols / 2)
y_medium = int(rows/2)
center = int(cols / 2)
center_y = int(rows/2)
pos_x = 70 # degrees
pos_y =120
n=0
frame_resizing = 0.25
while True:
    _, img = cap.read()
    #frame = cv2.resize(frame, (0, 0), fx = frame_resizing, fy=frame_resizing)

    if n%5 ==0:
        print(n)
        n = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Clasify face from the gray image
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            
        if faces is ():
            print('face not detct')
          
        else:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                # find the midpoint of the first face in the frame.
                xCentre = int(x + (w / 2))
                yCentre = int(y + (w / 2))
                cv2.circle(img, (xCentre, yCentre), 5, (0, 255, 255), -1)



                
            x_medium = xCentre
            y_medium = yCentre
            
            cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
            cv2.line(img, (0, y_medium), (640, y_medium), (0, 255, 0), 2)
            if x_medium < center -60:
                print("left")
                pos_x += 3
            if x_medium > center + 60:
                print('ringt')
                pos_x -= 3
            if y_medium <center_y - 40:
                print("up")
                pos_y += 2
            if y_medium > center_y + 40:
                print('down')
                pos_y -= 2
            angle(pos_y, pos_x)

    cv2.imshow("Frme", img)

    key = cv2.waitKey(1)
    n = n+1
    if key == 27:
        break  
cap.release()
cv2.destroyAllWindows()
