#!/usr/bin/python
# simple text box with configurable font size
# require the price as script argument
myFontSize = 60

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():

    app     = QtGui.QApplication(sys.argv)
    palette = QtGui.QPalette()
    label   = QtGui.QLabel("CIAO")

    palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.green)
    label.setPalette(palette)

    label.resize(800, 150)
    font = label.font()
    font.setPixelSize(myFontSize)
    label.setFont(font)

    label.setWindowTitle('PyQt QLabel Text Color')
    label.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()