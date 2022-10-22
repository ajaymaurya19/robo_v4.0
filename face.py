import dnn
import cv2 as cv
im = cv.imread('image.jpg')
_, bboxes = dnn.FaceDetector().process_frame(im, threshold=0.4) 
for i in bboxes:    
     cv.rectangle(im, (i[0], i[1]), (i[2], i[3]), (0, 255, 0), 3)
cv.imwrite('/image_output.jpg', im)