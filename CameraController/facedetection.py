import camera
import cv2

camera.init()
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

def getFaces():
    p = camera.getPhoto((300,300))
    image = cv2.imdecode(p, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    return faces
