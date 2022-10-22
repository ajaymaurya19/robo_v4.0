#!/usr/bin/python3
import jetson.inference
import jetson.utils
import cv2
#from main_video4 import img_reco


class mnSSD():
    def __init__(self, path= "ssd-mobilenet-v2", threshold= 0.5):
        self.path = path
        self.threshold = threshold
        self.net = jetson.inference.detectNet(self.path, self.threshold)
    
    def detect(self, img, display = False):
        imgCuda = jetson.utils.cudaFromNumpy(img)
        detections = self.net.Detect(imgCuda, overlay = "OVERLAY_NONE")
        objects = []
        #print(f'FPS: {int(self.net.GetNetworkFPS())}')
        for d in detections:
            className = self.net.GetClassDesc(d.ClassID)
            objects.append([className,d])
            
            if display:
                cx, cy = int(d.Center[0]),int(d.Center[1])
                x1,y1,x2,y2 = int(d.Left),int(d.Top),int(d.Right),int(d.Bottom)
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)
                cv2.circle(img, (cx,cy),5,(0,255,0),cv2.FILLED)
                cv2.line(img,(x1,cy),(x2,cy),(0,255,0),1)
                cv2.line(img,(cx,y1),(cx,y2),(0,255,0),1)
                cv2.putText(img, className, (x1+5,y1+5),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
                cv2.putText(img, f'FPS: {int(self.net.GetNetworkFPS())}', (30,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
        return objects

def main():
    import fn

    file_Name = fn.file_name()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/detecton.mp4',fourcc, 15.0, (640,480))
    
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    myModel = mnSSD()
    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        objects = myModel.detect(img,  True)
        '''if len(objects)!=0:
            #print(objects[0][0])
            if objects[0][0]=="person":
                #print(objects[0][0])
                #print(objects[0][0],img_reco(img, True))'''
        cv2.imshow("Image", img)
        out.write(img)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()

    out.release()
    
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
    '''import multiprocessing as mp
    q = mp.Queue() 
    #t3 = mp.Process(target= thred, args=(q,))
    t1 = mp.Process(target= main,args=(q,))
    
    
    cap = cv2.VideoCapture(0)
    
    from servokit import ServoKit
    kit = ServoKit()
    kit.angle(6, 250)
    kit.angle(7, 200)
    t1.start()
  
    from robo_tts import take_command, talk_gtts
    talk_gtts("hi",'en')
    while True:
        command = take_command()
        print(command)
        if command == 'can you see this' or 'see me' or 'tell me what is this ':
            q.put('face_reco')
        else:
            continue
    
    '''