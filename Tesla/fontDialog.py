__author__ = 'chenggu'

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setupUI()

    def setupUI(self):
        hbox = QtGui.QHBoxLayout()

        btn = QtGui.QPushButton('Dialog', self)
        btn.setFocusPolicy(QtCore.Qt.NoFocus)
        btn.move(20, 20)

        hbox.addWidget(btn)

        self.connect(btn, QtCore.SIGNAL('clicked()'), self.showDialog)

        self.label = QtGui.QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)

        self.setWindowTitle('FontDialog')
        self.setGeometry(300, 300, 250, 110)

    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())