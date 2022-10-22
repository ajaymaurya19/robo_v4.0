from re import I
import cv2
import pytesseract

# read image
#img = cv2.imread('/home/robo/Downloads/WhatsApp Video 2022-03-29 at 8.45.25 PM')
def img_to_text(img):
# Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    # OTSU threshold performing
    ret, threshimg = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    
    # Specifying kernel size and structure shape.  
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
    
    # Appplying dilation on the threshold image 
    dilation = cv2.dilate(threshimg, rect_kernel, iterations = 1) 
    
    # getting contours 
    img_contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                    cv2.CHAIN_APPROX_NONE) 
    
    # Loop over contours and crop and extract the text file
    for cnt in img_contours: 
        x, y, w, h = cv2.boundingRect(cnt) 
        
        # Drawing a rectangle
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        
        # Cropping the text block  
        cropped_img = img[y:y + h, x:x + w] 
        
        # Open the text file in append mode 
        file = open("recognized.txt", "a") 
        
        # Applying tesseract OCR on the cropped image 
        text = pytesseract.image_to_string(cropped_img)
        print(text)
        n = 25
        for te in text.split('\n'):
            if len(te)<2:
                pass
            else:
                cv2.putText(img, te,(50, n), cv2.FONT_HERSHEY_SIMPLEX,.7,(0,255,0),2)
                n=n+25
        
        # Appending the text into file 
        file.write(text) 
        file.write("\n") 
        
        # Close the file 
        file.close
    return img
 
        
if __name__ == "__main__":
    import fn
    import video_test
    file_Name = fn.file_name()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'/media/robo/nvidia/database/Video/imgtotext.mp4',fourcc, 15.0, (640,480))
    cap = cv2.VideoCapture('/home/robo/Downloads/WhatsApp Video 2022-03-29 at 8.45.25 PM')
    while True:
        _,img = cap.read()
        img = img_to_text(img)
        cv2.imshow("Image", img)
        out.write(img)     
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()