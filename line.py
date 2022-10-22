import cv2
import numpy as np
i




frames = [] # stores the video sequence for the demo

# Video capture parameters
(w, h) = (640,240)  # Resolution
bytesPerFrame = w * h
fps = 40 # setting to 250 will request the maximum framerate possible

lateral_search = 20 # number of pixels to search the line border
start_height = h - 5 # Scan index row 235

# "raspividyuv" is the command that provides camera frames in YUV format
#  "--output -" specifies stdout as the output
#  "--timeout 0" specifies continuous video
#  "--luma" discards chroma channels, only luminance is sent through the pipeline


cap = cv2.VideoCapture('/home/robo/Downloads/WhatsApp Video 2022-04-10 at 10.17.19 AM')
while True:
#for qwerty in xrange(500):
    _, img = cap.read()
   
    img.shape = (h,w) # set the correct dimensions for the numpy array for easier access to rows, now rows are columns

    frame_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) # Drawing color points requires RGB image
    # ret, thresh = cv2.threshold(frame, 105, 255, cv2.THRESH_BINARY)
    tresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    signed_thresh = thresh[start_height].astype(np.int16) # select on
    diff = np.diff(signed_thresh)   #The derivative of the start_height line

    points = np.where(np.logical_or(diff > 200, diff < -200)) #maximums and minimums of derivative

    cv2.line(frame_rgb,(0,start_height),(640,start_height),(0,255,0),1) # draw horizontal line where scanning 



        middle = (points[0][0] + points[0][1]) / 2

        cv2.circle(frame_rgb, (points[0][0], start_height), 2, (255,0,0), -1)
        cv2.circle(frame_rgb, (points[0][1], start_height), 2, (255,0,0), -1)
        cv2.circle(frame_rgb, (middle, start_height), 2, (0,0,255), -1)

     
    


  

