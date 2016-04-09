__author__ = 'chenggu'

import sys
from PyQt4 import QtGui

class Tooltip(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')

        self.setToolTip('This is a <b>QWidget</b> widget')

app = QtGui.QApplication(sys.argv)

tooltip = Tooltip()
tooltip.show()

sys.exit(app.exec_())