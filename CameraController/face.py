import picamera
import cv2
import io
import numpy
import time
from threading import Thread

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

def runner():
	global camera
	prev = None

	while True:
		stream = io.BytesIO()
		camera.capture(stream, format='jpeg')
		buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
		image = cv2.imdecode(buff, 1)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.1, 5)

		rect = numpy.zeros((240, 320, 3), dtype=numpy.uint8)
		for (x,y,w,h) in faces:
			rect[y, x:x+w, :] = 0xff
			rect[y+h, x:x+w, :] = 0xff
			rect[y:y+h, x, :] = 0xff
			rect[y:y+h, x+w, :] = 0xff
		if prev != None:
			camera.remove_overlay(prev)
		prev = camera.add_overlay(memoryview(rect), layer=4, alpha=64)
		print(str(len(faces)))

camera = picamera.PiCamera()

camera.resolution = (320, 240)
camera.rotation = 180

camera.start_preview()

try:
	Thread(target=runner).start()
except KeyboardInterrupt:
	camera.stop_preview()
