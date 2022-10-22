import cv2
import video_test
cap = cv2.VideoCapture(0) # 0 is camera device number, 0 is for internal webcam and 1 will access the first connected usb webcam
import fn
file_Name = fn.file_name()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frame_resizing = 0.5
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/vid{file_Name}.mp4',fourcc, 15.0, (640,480))
while True:
    


# Capture frame-by-frame
    ret, frame = cap.read()
  
    #frame = cv2.resize(frame, (0, 0), fx = frame_resizing, fy=frame_resizing)
    # mirror the frame
  
    frame = cv2.flip(frame, 1)
    out.write(frame)
     
    image = video_test.face_detector(frame)
    cv2.imshow('Video', image)
    # cv2.line(image, starting cordinates, ending cordinates, color, thickness)
    # left vertical line
   

    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
