
import cv2
def get():
        
        #cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture(0)
        while True:

                _, frame = cap.read()

                cv2.imshow("frame", frame)

                key = cv2.waitKey(1)
                if key == 27: #Key 'S'
                        break
        cv2.waitKey(0)
        cv2.destroyAllWindows() 



if __name__ == "__main__":
        get()
      
     