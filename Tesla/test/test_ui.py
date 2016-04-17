# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Sat Apr 16 19:00:16 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import re
import os
from git import Repo
from PyQt4 import QtCore, QtGui, uic

class Node(object):

    def __init__(self, commit, parent = None):

        self._commit = commit
        self._children = []
        self._parent = parent

        if parent is not None:
            parent.addChild(self)

    def addChild(self, child):
        self._children.append(child)

    def commit(self):
        return self._commit

    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    # def log(self, tabLevel = -1):
    #     output = ''
    #     tabLevel += 1
    #     for i in range(tabLevel):
    #         output += '\t'
    #     output += self._list + '\n'
    #
    #     for child in self._children:
    #         output += child.log(tabLevel)
    #
    #     tabLevel -= 1
    #
    #     return output
    #
    # def __repr__(self):
    #     return self.log()

class GitCommitModel(QtCore.QAbstractItemModel):


    filterRole = QtCore.Qt.UserRole + 1
    sortRole = QtCore.Qt.UserRole + 2

    """
    DIR = ''
    if DIR:
        repo = Repo(DIR)
    else:
        DIR = '/Users/chenggu/myQt/'
        repo = Repo(DIR)

    LIST = repo.git.log(oneline = True, graph = True, pretty = "%h %s %cd").split('\n')
    reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+)\s([a-zA-Z]+\s[a-zA-Z]+\s[0-9\s:]+)')
    """

    def __init__(self, root, parent = None):
        super(GitCommitModel, self).__init__(parent)
        self._rootNode = root

    def setDIR(self, dir):
        self.DIR = dir

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer() # call internalPointer to get the node

        return parentNode.childCount()

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return None

        node = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            if reGitInfo.match(node.commit()):
                if index.column() == 0:
                    return str(reGitInfo.match(node.commit()).groups()[0])
                elif index.column() == 1:
                    return str(reGitInfo.match(node.commit()).groups()[1])
                else:
                    return str(reGitInfo.match(node.commit()).groups()[2])

        if role == GitCommitModel.filterRole and reGitInfo.match(node.commit()):
            return str(reGitInfo.match(node.commit()).groups()[1])

        if role == GitCommitModel.sortRole and reGitInfo.match(node.commit()):
            return str(reGitInfo.match(node.commit()).groups()[2])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if section == 0:
                return "Commits"
            elif section == 1:
                return "Comments"
            else:
                return "Date"

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # return a QModelIndex
    def parent(self, index):

        node = self.getNode(index)
        parentNode = node.parent()

        if parentNode == self._rootNode:
            return QtCore.QModelIndex()

        # wrap the parentNode into a QModelIndex
        return self.createIndex(parentNode.row(), 0, parentNode)

    # return a QModelIndex
    def index(self, row, column, parent):

        parentNode = self.getNode(parent)

        childItem = parentNode.child(row)

        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def getNode(self, index):
        if index.isValid():
            node = index.internalPointer()
            if node:
                return node

        return self._rootNode

base, form = uic.loadUiType("widget.ui")

"""
class numberSortModel(QtGui.QSortFilterProxyModel):
    def lessThan(self, left, right):
        lvalue = left.data()[0]
        rvalue = right.data()[0]
        return lvalue < rvalue
"""


class window(base, form):

    def __init__(self, parent = None):
        super(base, self).__init__(parent)
        self.setupUi(self)

        # QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textEdited"), )
        # self.connect(self.lineEdit,QtCore.SIGNAL("textChanged(QString)"),
        #     self.lineEdit,QtCore.SLOT("setText(QString)"))

        rootNode   = Node("Git")

        i = 0
        count = 0
        flag = False

        if DIR:
            while i < len(LIST):
                if not reGitInfo.match(str(LIST[i])):
                    i += 1
                    if count % 2 == 0:
                        flag = True
                        count += 1
                    else:
                        flag = False
                        count += 1
                if not flag:
                    childNode = Node(str(LIST[i]), rootNode)
                    # self.treeWidget.topLevelItem(parent).setText(0, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[0]), None))
                    # self.treeWidget.topLevelItem(parent).setText(1, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[1]), None))
                    # parent += 1
                else:
                    childNode1 = Node(str(LIST[i]), childNode)
                    # self.treeWidget.topLevelItem(parent).child(children).setText(0, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[0]), None))
                    # self.treeWidget.topLevelItem(parent).child(children).setText(1, _translate("tesla_q3", str(self.reGitInfo.match(str(LIST[i])).groups()[1]), None))
                    # children += 1

                i += 1

        self._proxyModel = QtGui.QSortFilterProxyModel()

        self._model = GitCommitModel(rootNode)

        QtCore.QObject.connect(self.uiFilter, QtCore.SIGNAL("textChanged(QString)"), self._proxyModel.setFilterRegExp)

        self._proxyModel.setSourceModel(self._model)

        """
        self._proxyModel.setDynamicSortFilter(True)
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        """

        self._proxyModel.setSortRole(GitCommitModel.sortRole)
        self._proxyModel.setFilterRole(GitCommitModel.filterRole)


        # self._proxyModel.setFilterKeyColumn(0)

        self.uiTree.setModel(self._proxyModel)

        # self._proxyModel.setFilterRegExp("Right")

        self.uiTree.setSortingEnabled(True)

        # TODO: sort the commit time
        # QtGui.QAbstractProxyModel

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    DIR = '/Users/chenggu/myQt'
    repo = Repo(DIR)
    LIST = repo.git.log(oneline = True, graph = True, pretty = "%h %s %cd").split('\n')
    reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+)\s([a-zA-Z]+\s[a-zA-Z]+\s[0-9\s:]+)')

    wnd = window()
    wnd.show()

    sys.exit(app.exec_())