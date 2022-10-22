from pickle import NONE
import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime
from robo_tts import talk_gtts

now = datetime.now()
dtString = now.strftime('%d/%b/%Y, %H:%M:%S')
sfr = SimpleFacerec()
#sfr.load_encoding_images("/media/nvidi/nvidia/robo_AI/source code/images/")
def makeAttendanceEntry(name):
    with open('/media/nvidi/nvidia/robo_AI/source code/listt.csv','r+') as f:
        allLines = f.readlines()
        attendanceList = []
        for line in allLines:
            entry = line.split(',')
            attendanceList.append(entry[0])
        if name not in attendanceList:
            now = datetime.now()
            dtString = now.strftime('%d/%b/%Y, %H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def img_reco(img, display = True):
    face_locations, face_names = sfr.detect_known_faces(img)
    #print(face_locations,face_names)
    for face_loc, name in zip(face_locations, face_names):
        
      
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        #makeAttendanceEntry(name)
        #print('name')
        
        cv2.putText(img, name,(x1, y1 - 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(img, (x1-4, y1-54), (x2+4, y2+4), (0, 0, 200), 4)

        return img





if __name__=="__main__":
    from servokit import ServoKit
    kit = ServoKit()
    kit.angle(6, 100)
    kit.angle(7, 180)
    # Encode faces from a folder
    sfr = SimpleFacerec()
    #sfr.load_encoding_images("/media/robo/nvidia/database/images/")
    import fn
    import video_test
    file_Name = fn.file_name()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/vid{file_Name}.mp4',fourcc, 15.0, (640,480))
        
    # Load Camera
    cap = cv2.VideoCapture(0)
    cap.set(3,640.0) #set the size
    cap.set(4,480.0)  #set the size

    count = 0
    face_id = 7
    '''while True:
        _, img = cap.read()
        #_, img2 = cap.read()
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        #img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

            #cv2.imwrite("/media/word/nvidia/robo_AI/source code/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", frame[y1-50:y2,x1:x2])
            #count += 1
        frame = img_reco(img)
        #detect(img, img2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(0)
        if key == 27:
            break
        elif count >= 100: # Take 30 face sample and stop video
            break'''
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            #talk_gtts(name,'en')

        out.write(frame)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(0)
        if key == 27:
            break
