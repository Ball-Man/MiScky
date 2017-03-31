import UIController as uic
from UIController.types import Text

import time

uic.init()

WHITE = (255,255,255)

text1 = Text("Ciao", 50, WHITE)
text2 = Text("come stai?", 50, WHITE)

thread = uic.startPrintTextDiffuse(text1, (100,100), 1)
thread.join()
thread = uic.startPrintTextRunning(text2, 1, (200,200))
thread.join()

time.sleep(5)
pygame.quit()
