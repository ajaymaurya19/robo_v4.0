import cv2
import numpy as np
#from robo_move3 import angle
from servokit import ServoKit
kit = ServoKit()

# Set camera resolution.
cameraWidth = 640 
cameraHeight = 480

face_classifier = cv2.CascadeClassifier('/media/robo/nvidia/Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml')

# calculate the middle screen
midScreenX = int(cameraWidth / 2)
midScreenY = int(cameraHeight / 6)
midFaceX = int(cameraWidth / 2)
midFaceY = int(cameraHeight / 2)
midScreenWindow = 80
angle_x =250
angle_y = 200
kit.angle(6,int(angle_x))
kit.angle(7, int(angle_y))

def face_detector(img):
  
  
# Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Clasify face from the gray image
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    # print(localization)
    cv2.line(img, ((midScreenX - midScreenWindow), 0), ((midScreenX - midScreenWindow), cameraHeight), (255, 127, 0),2)
    # right vertical line
    cv2.line(img, ((midScreenX + midScreenWindow), 0), ((midScreenX + midScreenWindow), cameraHeight), (255, 127, 0),2)
    # up horizontal line
    cv2.line(img, (0, (midScreenY - midScreenWindow)), (cameraWidth, (midScreenY - midScreenWindow)), (255, 127, 0),2)
    # down horizontal line
    cv2.line(img, (0, (midScreenY + midScreenWindow)), (cameraWidth, (midScreenY + midScreenWindow)), (255, 127, 0),2)
    if faces is ():
        print('face not detct')
        return img

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # find the midpoint of the first face in the frame.
        xCentre = int(x + (w / 2))
        yCentre = int(y + (w / 2))
        cv2.circle(img, (xCentre, yCentre), 5, (0, 255, 255), -1)

       
        midFaceX = xCentre
        midFaceY = yCentre


    global angle_x 
    global angle_y 
    # Find out if the X component of the face is to the left of the middle of the screen.
    if (midFaceX < (midScreenX - midScreenWindow)):
        cv2.putText(img, "Move Left", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x =angle_x - 5
      
        
    # if(servoPanPosition >= 5):
    # servoPanPosition -= stepSize; #Update the pan position variable to move the servo to the left.
    if (midFaceX > (midScreenX + midScreenWindow)):
        cv2.putText(img, "Move Right", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x= angle_x + 5
        #angle(15, 120)
    if (midFaceY < (midScreenY - midScreenWindow)):
        cv2.putText(img, "Move Up", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(130, 70)
        angle_y = angle_y - 5
    if (midFaceY > (midScreenY + midScreenWindow)):
        cv2.putText(img, "Move Down", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(60, 70)
        angle_y = angle_y +5
    if angle_x >=100 and angle_x <= 400 and angle_y >=150 and angle_y <= 400:

        kit.angle(6,int(angle_x))
        kit.angle(7, int(angle_y))

    print(angle_x, angle_y)

    return img



