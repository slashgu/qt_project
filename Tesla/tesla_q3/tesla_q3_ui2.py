# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesla_q3.ui'
#
# Created: Thu Apr 14 17:50:40 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import re
import subprocess
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
7
class Ui_tesla_q3(QtGui.QWidget):
    def __init__(self):
        super(Ui_tesla_q3, self).__init__()
        self.setupUi(self)

    def setupUi(self, tesla_q3):
        tesla_q3.setObjectName(_fromUtf8("tesla_q3"))
        tesla_q3.resize(888, 666)
        self.verticalLayout = QtGui.QVBoxLayout(tesla_q3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.treeWidget = QtGui.QTreeWidget(tesla_q3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))

        self.button = QtGui.QPushButton('Search', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        QtGui.QWidget.sizeHint(self.button)

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItems(['day', 'week'])
        self.comboBox.activated.connect(self.setSearchRange)

        self.comboBox_num = QtGui.QComboBox(self)
        self.comboBox_num.addItems([str(i) for i in range(1, 11)])
        self.comboBox_num.activated.connect(self.setSearchNums)

        # TODO: build func
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.func)
        self.setFocus()

        repo = Repo(DIR)
        # repo = Repo('/Users/chenggu/Desktop/CS 5200/FinalProject')

        # SINCE = NUMS + '.' + RANGE
        # TODO
        # self.LIST = repo.git.log(oneline = True, graph = True, since = '').split('\n')
        self.reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+)')

        i = 0
        flag = False
        count = 0
        while i < len(LIST):
            if not self.reGitInfo.match(str(LIST[i])):
                i += 1
                if count % 2 == 0:
                    flag = True
                    count += 1
                else:
                    flag = False
                    count += 1
            if not flag:
                item_root = QtGui.QTreeWidgetItem(self.treeWidget)
            else:
                item_child = QtGui.QTreeWidgetItem(item_root)
            i += 1

        # add widget here
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.comboBox_num)
        self.verticalLayout.addWidget(self.button)
        # self.horizontalLayout.addWidget(self.treeWidget)
        # self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tesla_q3)
        QtCore.QMetaObject.connectSlotsByName(tesla_q3)

    def retranslateUi(self, tesla_q3):
        tesla_q3.setWindowTitle(_translate("tesla_q3", "tesla_q3", None))
        self.treeWidget.headerItem().setText(0, _translate("tesla_q3", "commits", None))
        self.treeWidget.headerItem().setText(1, _translate("tesla_q3", "comments", None))
        self.center()
        # self.treeWidget.headerItem().setText(2, _translate("tesla_q3", "author", None))

        i = 0
        count = 0
        flag = False
        parent = 0
        children = 0

        while i < len(LIST):
            if not self.reGitInfo.match(str(LIST[i])):
                i += 1
                if count % 2 == 0:
                    flag = True
                    count += 1
                    parent -= 1
                else:
                    flag = False
                    children = 0
                    count += 1
            if not flag:
                self.treeWidget.topLevelItem(parent).setText(0, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[0]), None))
                self.treeWidget.topLevelItem(parent).setText(1, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[1]), None))
                parent += 1
            else:
                self.treeWidget.topLevelItem(parent).child(children).setText(0, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[0]), None))
                self.treeWidget.topLevelItem(parent).child(children).setText(1, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[1]), None))
                children += 1

            i += 1

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry();
        size = self.geometry();
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def func(self):
        pass
        # SINCE = NUMS + '.' + RANGE
        # LIST = repo.git.log(oneline = True, graph = True, since = SINCE).split('\n')
        # # subprocess.Popen(['python', 'tesla_q3_ui2.py'])

    def setSearchRange(self):
        self.RANGE = str(self.comboBox.currentText())

    def setSearchNums(self):
        self.NUMS = str(self.comboBox_num.currentText())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    DIR = '/Users/chenggu/myQt/'
    repo = Repo(DIR)
    # repo = Repo('/Users/chenggu/Desktop/CS 5200/FinalProject')
    LIST = repo.git.log(oneline = True, graph = True).split('\n')
    # print type(LIST[0])
    # reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+)')
    ex = Ui_tesla_q3()
    ex.show()
    sys.exit(app.exec_())