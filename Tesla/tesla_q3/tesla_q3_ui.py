# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesla_q3.ui'
#
# Created: Wed Apr 13 15:35:47 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tesla_q3(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, tesla_q3):
        tesla_q3.setObjectName(_fromUtf8("tesla_q3"))
        tesla_q3.resize(527, 396)
        self.verticalLayout = QtGui.QVBoxLayout(tesla_q3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(tesla_q3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tesla_q3)
        QtCore.QMetaObject.connectSlotsByName(tesla_q3)

    def retranslateUi(self, tesla_q3):
        tesla_q3.setWindowTitle(_translate("tesla_q3", "tesla_q3", None))
        self.pushButton.setText(_translate("tesla_q3", "print name", None))
        self.pushButton.clicked.connect(self.printName)

    def printName(self):
        print "Cheng Gu"

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_tesla_q3()
    ex.show()
    sys.exit(app.exec_())


