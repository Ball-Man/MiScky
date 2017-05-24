#-*- coding:utf-8 -*-

import UIController as uic
from UIController.modules import *
import GoogleAPI.calendar as gcal
import GoogleAPI.gmail as gmail
import WeatherAPI as wapi
import CameraController as cam
import CameraController.facedetection as fdetect
import AudioController.audiocontroller as audio
import AudioController.tts as TTS
import pygame
import time
import datetime as dt
import json

NOW = dt.datetime.now

SLEEP_TIME = 1
CITY = 'Cesena'
CAMERA_ROTATION = 180
_started_time = NOW()

def checkKey():
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			return True
	return False

_lastPositionRead = dt.datetime.min
_position = {'calendar': (500,600), 'email': (500,50), 'weather': (50,300), 'clock': (50,50)}
def getModulePositions():
	global _lastPositionRead
	global _position
	if (NOW() - _lastPositionRead).total_seconds() > 5:
		with open('miscky.conf', 'r') as f:
			tmp = json.loads(f.read())
			_position = dict()
			for k in tmp:
				_position[k] = (tmp[k]['X'], tmp[k]['Y'])
		_lastPositionRead = NOW()
	return _position

_standby = True
def shouldStandby():
	global _standby
	if _standby and fdetect.facePresent():
		_standby = False
	return _standby

def speak():
	ora = NOW().strftime('%H e %M minuti')
	s = '.Buongiorno. Sono le {}. Per oggi e previsto: {}'.format(ora, wapi.todayWeather().description)
	TTS.playTTS(s)


def main():
	uic.init()
	wapi.init(CITY)
	cam.init(rotation=CAMERA_ROTATION)
	audio.init()
	_hasSpoken = False

	modules = []

	# Modules creation
	pos = getModulePositions()
	modules.append(CalendarModule((500,500), pos['calendar'], 29, gcal.getEvents))
	uic.addModule(modules[-1])
	modules.append(EmailModule((500,500), pos['email'], 37, gmail.get_unread))
	uic.addModule(modules[-1])
	modules.append(WeatherModule((300,300), pos['weather'], 100, wapi.todayWeather))
	uic.addModule(modules[-1])
	modules.append(ClockModule((300,210), pos['clock'], 1))
	uic.addModule(modules[-1])

	for m in modules:
		m.update()
	
	TTS.playTTS('.Specchio intelligente pronto. Prego, posizionarsi davanti allo specchio')
	time.sleep(6)

	while not checkKey():
		# Update all modules
		if not shouldStandby():
			if not _hasSpoken:
				speak()
				_hasSpoken = True
			for m in modules:
				m.update()
			uic.refresh()
		else:
			uic.standby()

		time.sleep(SLEEP_TIME)

if __name__ == '__main__':
	main()
