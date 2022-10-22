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
midScreenY = int(cameraHeight / 2)
midFaceX = int(cameraWidth / 2)
midFaceY = int(cameraHeight / 2)
midScreenWindow = 110
angle_x =300
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
        #cv2.circle(img, (xCentre, yCentre), 5, (0, 255, 255), -1)

       
        midFaceX = xCentre
        midFaceY = yCentre


    global angle_x 
    global angle_y 
    # Find out if the X component of the face is to the left of the middle of the screen.
    if (midFaceX < (midScreenX - midScreenWindow)):
        cv2.putText(img, "Move Left", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x =angle_x - 10
      
        
    # if(servoPanPosition >= 5):
    # servoPanPosition -= stepSize; #Update the pan position variable to move the servo to the left.
    if (midFaceX > (midScreenX + midScreenWindow)):
        cv2.putText(img, "Move Right", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x= angle_x + 10
        #angle(15, 120)
    if (midFaceY < (midScreenY - midScreenWindow)):
        cv2.putText(img, "Move Up", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(130, 70)
        angle_y = angle_y - 10
    if (midFaceY > (midScreenY + midScreenWindow)):
        cv2.putText(img, "Move Down", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(60, 70)
        angle_y = angle_y +10
    if angle_x >=100 and angle_x <= 400 and angle_y >=150 and angle_y <= 400:

        kit.angle(6,int(angle_x))
        kit.angle(7, int(angle_y))

    print(angle_x, angle_y)

    return img


# Open Webcam
import fn
import video_test
file_Name = fn.file_name()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/vid{file_Name}.mp4',fourcc, 15.0, (640,480))
    
cap = cv2.VideoCapture(0) # 0 is camera device number, 0 is for internal webcam and 1 will access the first connected usb webcam

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frame_resizing = 0.5
while True:
    


# Capture frame-by-frame
    ret, frame = cap.read()
  
    #frame = cv2.resize(frame, (0, 0), fx = frame_resizing, fy=frame_resizing)
    # mirror the frame
  
    frame = cv2.flip(frame, 1)
     
    image = face_detector(frame)
    out.write(image)
    cv2.imshow('Video', image)
    # cv2.line(image, starting cordinates, ending cordinates, color, thickness)
    # left vertical line
   

    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
