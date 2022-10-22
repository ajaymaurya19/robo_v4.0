import cv2
import numpy as np
#from robo_AI import setServoAngle
#from robo_move3 import angle
from servokit import ServoKit
kit = ServoKit()

cameraWidth = 640 
cameraHeight = 480

rows = 480
cols = 640
x_medium = int(cols / 2)
y_medium = int(rows/2)
center = int(cols / 2)
center_y = int(rows/2)
pos_x = 70 # degrees
pos_y =120
n=0
i=1
midScreenWindow = 110
angle_x =300
angle_y = 200
midFaceX = int(cameraWidth / 2)
midFaceY = int(cameraHeight / 2)
kit.angle(6,int(angle_x))
kit.angle(7, int(angle_y))
midScreenX = int(cameraWidth / 2)
midScreenY = int(cameraHeight / 2)
face_classifier = cv2.CascadeClassifier('/media/robo/nvidia/Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml')
import fn
import video_test
file_Name = fn.file_name()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/vid{file_Name}.mp4',fourcc, 15.0, (640,480))
 
def face_trc(img):
    global i,n,pos_x,pos_y
    n = n+1
    if n%10 ==0:
        print(n)
        n = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Clasify face from the gray image
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            
        if faces is ():
            '''print('face not detct')
            angle(120, 60)
            i = i+1
            if i==2:
                angle(120, 80)
                
            if i == 3:
                angle(130, 70)
            
            if i ==4:
                angle(110, 100)
                i=1'''
          
        else:
            i=1
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
            kit.angle(7, pos_x)
            kit.angle(8,pos_y)
    return img


def color_trc(frame):
    global n,pos_x,pos_y,angle_x, angle_y,midFaceX, midFaceY
    n = n+1
    if n%5 ==0:
        print(n)
        n = 0
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # red color
        lower_blue = np.array([90,60,0])
        upper_blue = np.array([121,255,255])
        lower_green = np.array([40,70,80])
        upper_green = np.array([70,255,255])
        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_frame, lower_blue,upper_blue)
        contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y),(x+w, y+h),(0,255,0),2)
            
            midFaceX= int((x + x + w) / 2)
            midFaceY= int((y+y+h)/2)
            break
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 0), 2)
        '''if x_medium < center -60:
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
        kit.angle(7, pos_x)
        kit.angle(8,pos_y)'''
    if (midFaceX < (midScreenX - midScreenWindow)):
        cv2.putText(frame, "Move Left", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x =angle_x - 10
      
        
    # if(servoPanPosition >= 5):
    # servoPanPosition -= stepSize; #Update the pan position variable to move the servo to the left.
    if (midFaceX > (midScreenX + midScreenWindow)):
        cv2.putText(frame, "Move Right", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        angle_x= angle_x + 10
        #angle(15, 120)
    if (midFaceY < (midScreenY - midScreenWindow)):
        cv2.putText(frame, "Move Up", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(130, 70)
        angle_y = angle_y - 10
    if (midFaceY > (midScreenY + midScreenWindow)):
        cv2.putText(frame, "Move Down", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #angle(60, 70)
        angle_y = angle_y +10
    if angle_x >=100 and angle_x <= 400 and angle_y >=150 and angle_y <= 400:

        kit.angle(6,int(angle_x))
        kit.angle(7, int(angle_y))

    print(angle_x, angle_y)
    return frame

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    cap.set(3,640.0) #set the size
    cap.set(4,480.0)
    while True:
        _, frame = cap.read()
        #frame = cv2.resize(frame, (0, 0), fx = frame_resizing, fy=frame_resizing)

        frame = face_trc(frame)
        out.write(frame)
        cv2.imshow("Frme", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break  
    cap.release()
    cv2.destroyAllWindows()
