import cv2
face_cascade=cv2.CascadeClassifier("C:/Users/ASUS/Desktop/haarcascade_frontalface_default.xml")

"""img = cv2.imread("C:/Users/ASUS/Desktop/WIN_20231225_19_46_56_Pro.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)"""

capture=cv2.VideoCapture(0)
while True:
    success,img=capture.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('image',img)
    if cv2.waitKey(20)==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()