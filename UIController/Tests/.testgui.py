#!/usr/bin/python
# simple text box with configurable font size
# require the price as script argument
myFontSize = 12

import time

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():

    app     = QtGui.QApplication(sys.argv)
    palette = QtGui.QPalette()
    label   = QtGui.QLabel("CIAO")

    palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
    label.setPalette(palette)

    label.resize(1920, 1080)
    font = label.font()
    font.setPixelSize(myFontSize)
    label.setFont(font)

    label.setWindowTitle('PyQt QLabel Text Color')
    label.show()
    time.sleep(5)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
