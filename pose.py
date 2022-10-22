#!/usr/bin/python3
import jetson.inference
import jetson.utils
import cv2
import math
#from main_video4 import img_reco

global n 
n=1
class mnSSD():
    def __init__(self, path= "resnet18-body", threshold= 0.15):
        self.path = path
        self.threshold = threshold
        self.net = jetson.inference.poseNet(self.path, self.threshold)
           
    def detect(self, img, display = False):
        global x_6 ,y_6, x_8, y_8,x_10,y_10,x_17,y_17,x_5,y_5, x_7,y_7,x_9,y_9,x_11,y_11,x_12,y_12,t_right_join_angle,t_right_join_angle, t_left_angle,t_right_angle,t_body_left_angle,t_body_left_angle,t_left_join_angle,t_body_right_angle
        global n 
        imgCuda = jetson.utils.cudaFromNumpy(img)
        #detections = self.net.Detect(imgCuda, overlay = "OVERLAY_NONE")
        poses = self.net.Process(imgCuda, overlay= "links,keypoints")
        objects = []
        #print(f'FPS: {int(self.net.GetNetworkFPS())}')
       
        for d in poses:
           
            for pos in d.Keypoints:
                cv2.circle(img, (int(pos.x), int(pos.y)), 5, (255, 0, 0), cv2.FILLED)
                #cv2.putText(img, str(pos.ID), (int(pos.x), int(pos.y)-5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                if pos.ID ==6:
                    x_6,y_6 = int(pos.x), int(pos.y)
                if pos.ID == 8:
                    x_8,y_8 = int(pos.x), int(pos.y)
                if pos.ID == 10:
                    x_10,y_10 = int(pos.x), int(pos.y)
                      

                if pos.ID ==5:
                    x_5,y_5 = int(pos.x), int(pos.y)
                if pos.ID == 7:
                    x_7,y_7= int(pos.x), int(pos.y)
                if pos.ID == 9:
                    x_9,y_9 = int(pos.x), int(pos.y)

                if pos.ID == 11:
                    x_11,y_11 = int(pos.x), int(pos.y)
                
                if pos.ID == 12:
                    x_12,y_12 = int(pos.x), int(pos.y)
                

              
                if pos.ID == 17:
                    x_17,y_17 = int(pos.x), int(pos.y)              


            cv2.line(img,(x_10,y_10), (x_8,y_8), (0,0,255),2) 
            cv2.line(img,(x_8,y_8), (x_6,y_6), (0,0,255),2)
            cv2.line(img,(x_6,y_6), (x_17,y_17), (0,0,255),2)
            cv2.line(img,(x_17,y_17), (x_5,y_5), (0,0,255),2)
            cv2.line(img,(x_5,y_5), (x_7,y_7), (0,0,255),2)
            cv2.line(img,(x_7,y_7), (x_9,y_9), (0,0,255),2)

            cv2.line(img,(x_6,y_6), (x_12,y_12), (0,0,255),2)
            cv2.line(img,(x_5,y_5), (x_11,y_11), (0,0,255),2)
            left_join_angle = math.degrees(math.atan2(y_10 - y_8, x_10 - x_8) -
                                math.atan2(y_6 - y_8, x_6 - x_8))
            right_join_angle = math.degrees(math.atan2(y_9 - y_7, x_9 - x_7) -
                             math.atan2(y_5 - y_7, x_5 - x_7))
            left_angle = math.degrees(math.atan2(y_8 - y_6, x_8 - x_6) -
                             math.atan2(y_17 - y_6, x_17 - x_6))
            right_angle = math.degrees(math.atan2(y_7 - y_5, x_7 - x_5) -
                             math.atan2(y_17 - y_5, x_17 - x_5))
            body_left_angle = math.degrees(math.atan2(y_8 - y_6, x_8 - x_6) -
                             math.atan2(y_12 - y_6, x_12 - x_6))
            body_right_angle = math.degrees(math.atan2(y_7 - y_5, x_7 - x_5) -
                             math.atan2(y_11 - y_5, x_11 - x_5))
            
            if left_join_angle < 0:
                left_join_angle = -left_join_angle
            if right_join_angle < 0:
                right_join_angle = -right_join_angle
            if left_angle < 0:
                left_angle = -left_angle
            if right_angle < 0:
                right_angle = -right_angle
            if body_left_angle < 0:
                body_left_angle = -body_left_angle
            if body_right_angle < 0:
                body_right_angle = -body_right_angle
            
            if left_join_angle > 180:
                left_join_angle = left_join_angle -360
            if right_join_angle > 180:
                right_join_angle = right_join_angle-360
            if left_angle > 180:
                left_angle = left_angle-360
            if right_angle > 180:
                right_angle = right_angle-360
            if body_left_angle > 180:
                body_left_angle = body_left_angle-360
            if body_right_angle > 180:
                body_right_angle = body_right_angle-360
            
            if left_join_angle < 0:
                left_join_angle = -left_join_angle
            if right_join_angle < 0:
                right_join_angle = -right_join_angle
            if left_angle < 0:
                left_angle = -left_angle
            if right_angle < 0:
                right_angle = -right_angle
            if body_left_angle < 0:
                body_left_angle = -body_left_angle
            if body_right_angle < 0:
                body_right_angle = -body_right_angle


            if n ==1:
                cv2.putText(img, str(int(left_angle)), (50, 50),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(left_join_angle)), (50, 75),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(body_left_angle)), (50, 100),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)

                
                cv2.putText(img, str(int(right_angle)), (570, 50),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(right_join_angle)), (570, 75),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(body_right_angle)), (570, 100),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                
                
                t_left_join_angle = left_join_angle
           
                t_right_join_angle = right_join_angle
          
                t_left_angle = left_angle
        
                t_right_angle = right_angle
         
                t_body_left_angle = body_left_angle
           
                t_body_right_angle = body_right_angle
                n = n+1
            else:
                if t_left_join_angle > left_join_angle +30 or t_left_join_angle < left_join_angle - 30:
                 
                    t_left_join_angle = left_join_angle

                if t_right_join_angle >right_join_angle +30 or t_right_join_angle < right_join_angle - 30:

                    t_right_join_angle = right_join_angle
                
                if t_left_angle >left_angle +30 or t_left_angle < left_angle - 30:

                    t_left_angle = left_angle
                
                if t_right_angle >right_angle +30 or t_right_angle < right_angle - 30:

                    t_right_angle = right_angle
                
                if t_body_left_angle >body_left_angle +30 or t_body_left_angle < body_left_angle - 30:

                    t_body_left_angle = body_left_angle
                
                if t_body_right_angle >body_right_angle +30 or t_body_right_angle < body_right_angle - 30:

                    t_body_right_angle = body_right_angle



                cv2.putText(img, str(int(t_left_join_angle)), (x_8, y_8-5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                
                cv2.putText(img, str(int(t_left_angle)), (x_6, y_6-5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(t_body_left_angle)), (x_6, y_6+10),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(t_right_join_angle)), (x_7,y_7-5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, str(int(t_right_angle)), (x_5,y_5-5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                
                cv2.putText(img, str(int(t_body_right_angle)), (x_5,y_5+10),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
             
           
def main():
  
    cap = cv2.VideoCapture(0)
  
    cap.set(3,640)
    cap.set(4,480)
    myModel = mnSSD()
    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        objects = myModel.detect(img,  True)
     
        cv2.imshow("Image", img)
      
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()