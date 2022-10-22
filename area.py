import cv2
import numpy as np


def get_area(img, colour, display = False):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow("in", imgHsv)

    lower_yellow = np.array([25,70,120])
    upper_yellow = np.array([30,255,255])

    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,120])
    upper_red = np.array([10,255,255])

    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])
    global area
    mask1 = cv2.inRange(imgHsv,lower_yellow,upper_yellow)
    mask2 = cv2.inRange(imgHsv,lower_green,upper_green)
    mask3 = cv2.inRange(imgHsv,lower_red,upper_red)
    mask4 = cv2.inRange(imgHsv,lower_blue,upper_blue)

    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours1 = imutils.grab_contours(contours1)

    contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours2 = imutils.grab_contours(contours2)

    contours3, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours3 = imutils.grab_contours(contours3)

    contours4, hierarchy = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours4 = imutils.grab_contours(contours4)
    if colour == "yellow":
        contours_c = contours1
    if colour == "green":
        contours_c = contours2
    if colour == "red":   
        contours_c = contours3
    if colour == "blue":
        contours_c = contours4

    for cnt in contours_c:
        area = cv2.contourArea(cnt)

        if area > 5000:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)

            M = cv2.moments(cnt)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(img,(cx,cy),7,(255,255,255),-1)

            cv2.putText(img, colour , (cx -  20, cy - 20), cv2.FONT_HERSHEY_COMPLEX, 2.5,
                        (0, 255, 0), 3)
    if display:
        cv2.imshow("ing",img)
    ar = int(area)
    return ar

if __name__ == "__main__":
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

    while True:

        _, img = cap.read()
        rea =get_area(img, "green",True)
        if rea> 0:
            print(rea)



        
        
        k= cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.distroyAllWindows()