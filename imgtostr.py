from PIL import Image
import numpy as np
import pytesseract
import cv2


cont =1
def img_to_str(img):
    global cont 
    text =''
    
    temp = ''
    n =100
    texts = []
    imgboxes =''
    cont = cont + 1
    imgh, imgw,_ = img.shape
    if 0 ==0:
        
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_thresh = cv2.adaptiveThreshold(img,    
               255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,81,11)
        cv2.imshow("Imag", img_thresh)
       



        imgboxes= pytesseract.image_to_boxes(img_thresh,lang='eng')
        text = pytesseract.image_to_string(img_thresh,lang='eng')
        '''if cont < 15:
            f = open('/media/password/nvidia/robo_AI/text.txt', "a")
            f.write(f'\n{text}')
            f.close()
            temp = text
        elif len(text)>len(temp):
            f = open('/media/password/nvidia/robo_AI/text.txt', "a")
            f.write(f'\n{text}')
            f.close()
            temp = text
        else:
            pass       
       
        print("readed")'''
        print(text)
    '''if cont> 70:
        break'''
    n=100
    for txt in text.split('\n'):
        if len(txt)<1:
            pass
        else:
            texts.append(txt)
    print(texts)
    for boxex in imgboxes.splitlines():
        boxex = boxex.split(' ')
        x,y,w,h = int(boxex[1]),int(boxex[2]),int(boxex[3]),int(boxex[4])
        cv2.rectangle(img,(x, imgh-y), (w, imgh - h), (0,0,255),1)
        cv2.putText(img, boxex[0],(x, imgh-y), cv2.FONT_HERSHEY_SIMPLEX,.7,(0,255,0),2)
    for txt in texts:
        cv2.putText(img,txt,(10,10),cv2.FONT_HERSHEY_SIMPLEX,.7,(255,0,0),2)
        #cv2.putText(img,str(len(txt)),(500,int(n)),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,255,0),2)
        n = n+30
    texts.clear()
    return img
if __name__=='__main__':
    cap = cv2.VideoCapture('/home/robo/Downloads/WhatsApp Video 2022-03-29 at 8.45.25 PM')
    cap.set(3,640.0) #set the size
    cap.set(4,480.0)  #set the size

    while True:
        _, img = cap.read()
        img = img_to_str(img)
        cv2.imshow("Image", img)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

            
    cap.release()
    cv2.destroyAllWindows()
