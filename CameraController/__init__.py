import picamera
import io
import numpy

camera = None

def init(rotation = 0):
	#Initialize the camera module. If it's already initialized does nothing
	global camera
	if rotation not in [0, 90, 180, 270]:
		raise ValueError('Invalid rotation value')
	if camera == None:
		camera = picamera.PiCamera()
		camera.rotation = rotation

def getPhoto(resolution=(1920,1080)):
	# Captures a photo with the given resolution and returns it as a io.BytesIO
	if not (isinstance(resolution, (tuple, list)) and len(resolution) == 2 and all(map(lambda x: isinstance(x, int), resolution)) and all(map(lambda x: int(x) > 0, resolution))):
		raise ValueError('Invalid resolution')

	global camera
	camera.resolution = resolution
	stream = io.BytesIO()
	camera.capture(stream, format='jpeg')
	return numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
