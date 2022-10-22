import cv2
import numpy as np



def get_color(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    return frame
def get_area(img, colour, display = False):
    lower_black = np.array([0,0,0])
    upper_black = np.array([179,255,10])
    lower_yellow = np.array([25,70,120])
    upper_yellow = np.array([30,255,255])

    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,120])
    upper_red = np.array([10,255,255])
    
    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow("in", imgHsv)

  
    global area
    mask1 = cv2.inRange(imgHsv,lower_yellow,upper_yellow)
    mask2 = cv2.inRange(imgHsv,lower_green,upper_green)
    mask3 = cv2.inRange(imgHsv,lower_red,upper_red)
    mask4 = cv2.inRange(imgHsv,lower_blue,upper_blue)
    mask5 = cv2.inRange(imgHsv,lower_black,upper_black)

    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  

    contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    contours3, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    contours4, hierarchy = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours5, hierarchy = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    if colour == "yellow":
        contours_c = contours1
    if colour == "green":
        contours_c = contours2
    if colour == "red":   
        contours_c = contours3
    if colour == "blue":
        contours_c = contours4
    if colour == "black":
        contours_c = contours5

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
        cv2.imshow("i",mask5)
   
    return area
if __name__ =="__main__":
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

    while True:

        _, img = cap.read()
        rea =get_area(img, "yellow",True)
    
        print(rea)
        #img = get_color(img)
        #cv2.imshow("img",img)
        
        k= cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.distroyAllWindows()