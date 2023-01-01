import cv2
from obj_detection import *
import time
from area_ import get_color, get_area
from control_fun2 import face_trc, color_trc
from simple_facerec import SimpleFacerec


def cam(q):
    cap = cv2.VideoCapture(0)
    cap.set(3,640) #set the size
    cap.set(4,480)  #set the size
    import fn
    import video_test
    file_Name = fn.file_name()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/vid{file_Name}.mp4',fourcc, 15.0, (640,480))
    print("cap")
    detect = True
    line_follower = False
    colour_detect = False
    follow_obj = False
    faces_trc = False
    colour_trc = False
    face_reco = True
    take_pic = False
    vid_record = False
    speak_reco = False
    speak_detect = False
    from robo_tts import talk_gtts
    myModel = mnSSD()
    data = ''
    while True:
        #data =  conn.recv()
        _, img = cap.read()
        img = cv2.flip(img, 1)
        if not q.empty():
            data = q.get()
            if data == "detect":
              
                line_follower = False
                colour_detect = False
                follow_obj = False
                faces_trc = False
                colour_trc = False
                detect = True
               
            elif data == "follow_line":
                detect = False
           
                colour_detect = False
                follow_obj = False
                faces_trc = False
                colour_trc = False
                line_follower = True
            
            elif data == "detect colour":
                detect = False
            elif data== "detect stop":
                detect = False
            elif data == "follow object":
                detect = False
                line_follower = False
                colour_detect = False
             
                faces_trc = False
                colour_trc = False
                follow_obj = True
            
            elif data == "face_trc":
                detect = False
                line_follower = False
                colour_detect = False
                follow_obj = False
             
                colour_trc = False
                faces_trc = True

            elif data == "color_trc":
                detect = False
                line_follower = False
                colour_detect = False
                follow_obj = False
                faces_trc = False
            
                colour_trc = True
            elif data == "face_reco":
                face_reco = True
            elif data == 'speak_reco':
                speak_reco = True
            elif data == 'speak_detect':
                speak_detect = True
           
        if detect:
                objects = myModel.detect(img,  True)
                if len(objects)!=0:
                    #print(objects[0][0])
                    if speak_detect:
                        if objects[0][0]=="person":
                            talk_gtts(f'Hello Ajay ', 'en')
                        else:
                            talk_gtts(f'yes...  this is {objects[0][0]}', 'en')
                    speak_detect = False
        if face_reco:
            #img_reco(img, True)
            #print('reco')
            sfr = SimpleFacerec()
            #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            
            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(img)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(img, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 200), 4)
                if speak_reco:
                    if name =='unknown':
                        talk_gtts('i never see you before', 'en')
                    elif name == "Ajay":
                        talk_gtts('Hello, Ajay Happy birthday', 'en')

                    else:

                        talk_gtts(f'hi.. {name} how are you', 'en')
                speak_reco = False

        if follow_obj:
            rea =get_area(img, "yellow",True)
            print(rea)
        if colour_detect:
            img = get_color(img)
        if colour_trc:
            color_trc(img)
        if faces_trc:
            face_trc(img)
        if take_pic:
            import fn
            file_Name = fn.file_name()
            robo_tts.talk_gtts('Be ready!...... 3.....2........1..........')
            cv2.imwrite(f'/media/robo/nvidia/database/images/image{file_Name}.png',img)
            take_pic = False
        if vid_record:
            #img = cv2.flip(img, 1)
            out.write(img)
            
            img = video_test.face_detector(img)
        #img = cv2.flip(img, 1)
        out.write(img)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if data == "END":
            break
        if key ==27:
            break

    print('stop')

      
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
    import multiprocessing as mp
    q = mp.Queue() 
    #t3 = mp.Process(target= thred, args=(q,))
    t1 = mp.Process(target= cam,args=(q,))
    t1.start()
    from robo_tts import take_command, talk_gtts
    talk_gtts("hi",'en')
    while True:
        command = take_command()
        print(command)
        '''if command == 'can you see me' or 'see me' or 'tell me my name':
            q.put('face_reco')'''
        if command == 'can you see this' or 'see this' or 'tell me what is this' or 'detect this':
            print('detection')
            q.put('detect')
        else:
            continue