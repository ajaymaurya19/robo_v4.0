import numpy as np
import cv2
from robo_move4 import *
from servokit import ServoKit
kit = ServoKit()
angle_x =250
angle_y = 350
kit.angle(6,int(angle_x))
kit.angle(7, int(angle_y))

dis = DistanceSensor()
def linefollow(frame):
    if 32 > 20:
        #frame = frame[150:480, 0:640]
        kernel = np.ones((2,2),np.uint8)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
        gray = cv2.GaussianBlur(gray, (5 ,5), 0)
        threshold1 = 80
        threshold2 = 80
        edged = cv2.Canny(gray, threshold1, threshold2)
    
      
      
        
        #to strength week pixels
        thresh = cv2.dilate(edged,kernel,iterations = 5)
        cv2.imshow('thrh',thresh)
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.line(frame, (220,0), (220, 480), (255,0,0),3)
        cv2.line(frame, (420,0), (420, 480), (255,0,0),3)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)
            cv2.drawContours(frame, contours, -1, (0,255,0), 1)
            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
            
            print(cx)
            if cx >= 420:
                print ("Turn Left!")
                motor_con('goleft')
                
            elif cx < 420 and cx > 220:
                print ("On Track!")
                motor_con('goforward')
            elif cx <= 220:
                
                print("Turn Right")

                motor_con("goright")
                
                
            else:
                print ("I don't see the line")
                motor_con('stop')
if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3,640.0) #set the size
    cap.set(4,480.0)  #set the size

    
    while(True):
    
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        #if dis.getDistance() > 20:
     
        linefollow(frame)
      
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    cap.release()
    cv2.destroyAllWindows()
