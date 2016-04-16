# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesla_q3.ui'
#
# Created: Thu Apr 14 17:50:40 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import re
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

        # item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtGui.QTreeWidgetItem(self.treeWidget)
        i = 0
        flag = False
        count = 0
        while i < len(list):
            if not reGitInfo.match(str(list[i])):
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

            # if reGitInfo.match(str(item)):
            #     item_1 = QtGui.QTreeWidgetItem(self.treeWidget)
            # else:
            #     item_2 = QtGui.QTreeWidgetItem(item_1)


        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tesla_q3)
        QtCore.QMetaObject.connectSlotsByName(tesla_q3)

    def retranslateUi(self, tesla_q3):
        headCommit = repo.head.commit
        tesla_q3.setWindowTitle(_translate("tesla_q3", "tesla_q3", None))
        self.treeWidget.headerItem().setText(0, _translate("tesla_q3", "commits", None))
        self.treeWidget.headerItem().setText(1, _translate("tesla_q3", "comments", None))
        # self.treeWidget.headerItem().setText(2, _translate("tesla_q3", "author", None))
        i = 0
        count = 0
        flag = False
        parent = 0
        children = 0

        while i < len(list):
            if not reGitInfo.match(str(list[i])):
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
                self.treeWidget.topLevelItem(parent).setText(0, _translate("tesla_q3", str(reGitInfo.match(str(list[i])).groups()[0]), None))
                self.treeWidget.topLevelItem(parent).setText(1, _translate("tesla_q3", str(reGitInfo.match(str(list[i])).groups()[1]), None))
                print reGitInfo.match(str(list[i])).groups()
                parent += 1
            else:
                self.treeWidget.topLevelItem(parent).child(children).setText(0, _translate("tesla_q3", str(reGitInfo.match(str(list[i])).groups()[0]), None))
                self.treeWidget.topLevelItem(parent).child(children).setText(1, _translate("tesla_q3", str(reGitInfo.match(str(list[i])).groups()[1]), None))
                print reGitInfo.match(str(list[i])).groups()
                children += 1

            i += 1

        # for item in list:
        #     if reGitInfo.match(str(item)):
        #         self.treeWidget.topLevelItem(i).setText(0, _translate("tesla_q3", str(reGitInfo.match(str(item)).groups()[0]), None))
        #         self.treeWidget.topLevelItem(i).setText(1, _translate("tesla_q3", str(reGitInfo.match(str(item)).groups()[1]), None))
        #         i += 1
        #
        #         # self.treeWidget.topLevelItem(i).setText(2, _translate("tesla_q3", commits[i].author.name, None))
        #     else:
        #         pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    repo = Repo('/Users/chenggu/myQt/')
    stack = []
    list = repo.git.log(oneline = True, graph = True).split('\n')
    reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+)')
    # commits = list(repo.iter_commits())
    ex = Ui_tesla_q3()
    ex.show()
    sys.exit(app.exec_())