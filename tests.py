import time

from UIController.modules import *
import UIController as uic

uic.init()

# Create calendar object. Events as strings
calendar = CalendarModule(events=["evento1", "festa bella", "alo che fa il leso"])

meteo = MeteoModule(temperature=20, minTemperature=10, maxTemperature=25, weather=MeteoModule.SUNNY)

uic.addModule(calendar, (50, uic.screen.height/2))
uic.refresh()
time.sleep(5)
uic.addModule(meteo, (500, uic.screen.height/2))
uic.refresh()
time.sleep(5)
uic.removeModule(calendar)
uic.refresh()
time.sleep(10)
