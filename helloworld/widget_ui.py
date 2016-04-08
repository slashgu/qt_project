# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Fri Apr  8 15:28:13 2016
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

class Ui_Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(406, 338)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.printHam_btn = QtGui.QPushButton(Widget)
        self.printHam_btn.setObjectName(_fromUtf8("printHam_btn"))
        self.verticalLayout.addWidget(self.printHam_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Super Ham", None))
        self.printHam_btn.setText(_translate("Widget", "Print Ham", None))
        self.printHam_btn.clicked.connect(self.printHam)

    def printHam(self):
        print ("Ham!")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Widget()
    ex.show()
    sys.exit(app.exec_())

