import cv2
import numpy as np

def canny (image):
    gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #blur= cv2.GaussianBlur (gray, (5, 5),0)
    canny = cv2.Canny (gray, 80, 150)
    return canny

def region_of_interest(image):
    height=image.shape [0]
    width=image.shape[1]
    #this has to be modified
    #polygons = np.array([[(10,height), (width,height), (width//2,height//2)]])
    polygons= np.array([[(50, height), (width / 2 - 20, height / 2 + 50 ),
                             (width / 2 + 50, height / 2 + 50), (width - 20, height)]], dtype=np.int32)
    mask = np.zeros_like (image)
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask) 
    return masked_image

def display_lines(frame,lines):
    line_frame=np.zeros_like(frame)
    if lines is not None:
        for  line in lines:
          x1,y1,x2,y2=line[0]
          cv2.line(line_frame,(x1,y1),(x2,y2),(0,255,0),10)
    return line_frame

cap = cv2.VideoCapture("C:/Users/ASUS/Downloads/Video1.mp4")
while(cap. isOpened()):
    _, frame = cap.read()
    lane_frame = np.copy(frame)

    canny_image=canny(frame)
    croped_image=region_of_interest(canny_image)

    # Apply Hough Line Transform (Probabilistic Hough Line Transform)
    lines =cv2.HoughLinesP(croped_image,rho=3,theta=np.pi/180,threshold=140, minLineLength=60,maxLineGap=5)

    # Draw the detected lines on a copy of the original frame
    line_frame =display_lines(lane_frame,lines)
    combo_frame=cv2.addWeighted(frame,0.8,line_frame,1,1)

    # Display the frame with detected lines
    cv2.imshow('Lane Detection',combo_frame)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


