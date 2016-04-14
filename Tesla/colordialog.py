__author__ = 'chenggu'

import sys
from PyQt4 import QtCore, QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUI()

    def setupUI(self):
        color = QtGui.QColor(0, 0, 0)

        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()

        self.widget = QtGui.QWidget(self)
        self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())
        self.widget.setGeometry(130, 22, 100, 100)

        self.setWindowTitle('ColorDialog')
        self.setGeometry(300, 300, 250, 180)

    def showDialog(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.widget.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())