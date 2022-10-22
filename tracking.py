import cv2
tracker = cv2.legacy.TrackerMOSSE_create()
def drawBox(img,bbox):

    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def trc(img, bbox):
    global p
    if 1==1:
        if p ==1:
            faces= bbox[0]

            tracker.init(img, faces)
                    #drawBox(img,faces)
       
            p= p+1
        if p>1:          
            success, bbox = tracker.update(img)
            if success:
                drawBox(img,bbox)
            else:
                cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    return img
  
########################################################
m =1
p=1
cap = cv2.VideoCapture(0)
cap.set(3,640.0) #set the size
cap.set(4,480.0)

n =1


face_classifier = cv2.CascadeClassifier('/media/robo/nvidia/Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml')
def face_trc(img):
    global i,n,pos_x,pos_y
    n = n+1

    if n%1 ==0:
     
        n = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Clasify face from the gray image
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)    
        if faces is ():
            print('face not detct')
            return  faces
        else:
            i=1
            print(faces)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                # find the midpoint of the first face in the frame.
                xCentre = int(x + (w / 2))
                yCentre = int(y + (w / 2))
                cv2.circle(img, (xCentre, yCentre), 5, (0, 255, 255), -1)
            return  faces


if __name__ =="__main__":
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        if m==1:    
            faces = face_trc(img)
            m = m+1 
        if m>1:

            if faces is ():
                faces = face_trc(img)
            
            else:
                img = trc(img,faces)
    
        cv2.imshow("img", img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break