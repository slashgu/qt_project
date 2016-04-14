# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesla_q3.ui'
#
# Created: Thu Apr 14 17:50:40 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from git import Repo
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
    def __init__(self):
        super(Ui_tesla_q3, self).__init__()
        self.setupUi(self)

    def setupUi(self, tesla_q3):
        tesla_q3.setObjectName(_fromUtf8("tesla_q3"))
        tesla_q3.resize(678, 486)
        self.verticalLayout = QtGui.QVBoxLayout(tesla_q3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.treeWidget = QtGui.QTreeWidget(tesla_q3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)

        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tesla_q3)
        QtCore.QMetaObject.connectSlotsByName(tesla_q3)

    def retranslateUi(self, tesla_q3):
        headCommit = repo.head.commit
        tesla_q3.setWindowTitle(_translate("tesla_q3", "tesla_q3", None))
        self.treeWidget.headerItem().setText(0, _translate("tesla_q3", "commits", None))
        self.treeWidget.headerItem().setText(1, _translate("tesla_q3", "comments", None))
        self.treeWidget.topLevelItem(0).setText(0, _translate("tesla_q3", str(headCommit), None))
        self.treeWidget.topLevelItem(0).setText(1, _translate("tesla_q3", headCommit.message, None))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("tesla_q3", "test", None))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("tesla_q3", "test message", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    repo = Repo('/Users/chenggu/myQt/')
    ex = Ui_tesla_q3()
    ex.show()
    sys.exit(app.exec_())