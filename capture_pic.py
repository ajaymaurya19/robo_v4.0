import cv2
from threading import Thread
import fn

def read_img():
    img1 = cv2.imread(f"face/{file_Name}.jpg")
    cv2.imshow(f"{file_Name}", img1)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
def strt():
    Thread(target=read_img, args=()).start()
    
videoCaptureObject = cv2.VideoCapture(0)
result = True
n =1
while(result):
    n = n+1
    ret,frame = videoCaptureObject.read()
    if n == 100:
        file_Name = fn.file_name()
        cv2.imwrite(f"face/{file_Name}.jpg",frame)
        strt()
        n=1
    cv2.imshow("fram", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            break
videoCaptureObject.release()
cv2.destroyAllWindows()