import cv2
import random

img=cv2.imread('INPUT.png')

font = cv2.FONT_HERSHEY_COMPLEX

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  
# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for index,contour in enumerate(contours):
    if index!=0:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        x,y,w,h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        
        blue_color=random.randint(0,255)
        green_color=random.randint(0,255)
        red_color=random.randint(0,255)
        color=(blue_color,green_color,red_color)
        
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        
        if area>1000:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img, str(index), (cx, cy), 
                          font, 0.5, color)

        print(area)
        cv2.imwrite('sample_output.png',img)
        print(x,y,w,h)