# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\kille\Documents\Programming\Python\IA\UIs\MainScreenUIDraft.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(674, 457)
        self.ViewAndEdit = QtWidgets.QPushButton(Dialog)
        self.ViewAndEdit.setGeometry(QtCore.QRect(410, 80, 241, 71))
        self.ViewAndEdit.setObjectName("ViewAndEdit")
        self.Ignored = QtWidgets.QPushButton(Dialog)
        self.Ignored.setGeometry(QtCore.QRect(410, 170, 241, 71))
        self.Ignored.setObjectName("Ignored")
        self.BlockedList = QtWidgets.QPushButton(Dialog)
        self.BlockedList.setGeometry(QtCore.QRect(410, 270, 241, 71))
        self.BlockedList.setObjectName("BlockedList")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(20, 0, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.MainTable = QtWidgets.QTableWidget(Dialog)
        self.MainTable.setGeometry(QtCore.QRect(10, 80, 391, 261))
        self.MainTable.setObjectName("MainTable")
        self.MainTable.setColumnCount(3)
        self.MainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, item)
        self.SaveButton = QtWidgets.QPushButton(Dialog)
        self.SaveButton.setGeometry(QtCore.QRect(10, 360, 91, 31))
        self.SaveButton.setObjectName("SaveButton")
        self.IgnoredText = QtWidgets.QLabel(Dialog)
        self.IgnoredText.setGeometry(QtCore.QRect(220, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IgnoredText.setFont(font)
        self.IgnoredText.setText("")
        self.IgnoredText.setObjectName("IgnoredText")
        self.EditButton = QtWidgets.QPushButton(Dialog)
        self.EditButton.setGeometry(QtCore.QRect(120, 360, 91, 31))
        self.EditButton.setObjectName("EditButton")
        self.SearchBar = QtWidgets.QLineEdit(Dialog)
        self.SearchBar.setGeometry(QtCore.QRect(370, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SearchBar.setFont(font)
        self.SearchBar.setObjectName("SearchBar")
        self.GoButton = QtWidgets.QPushButton(Dialog)
        self.GoButton.setGeometry(QtCore.QRect(630, 20, 31, 31))
        self.GoButton.setObjectName("GoButton")
        self.NumberEdit = QtWidgets.QLineEdit(Dialog)
        self.NumberEdit.setGeometry(QtCore.QRect(490, 390, 141, 21))
        self.NumberEdit.setObjectName("NumberEdit")
        self.SETButton = QtWidgets.QPushButton(Dialog)
        self.SETButton.setGeometry(QtCore.QRect(630, 390, 31, 21))
        self.SETButton.setObjectName("SETButton")
        self.RefreshButton = QtWidgets.QPushButton(Dialog)
        self.RefreshButton.setGeometry(QtCore.QRect(590, 350, 51, 31))
        self.RefreshButton.setObjectName("RefreshButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ViewAndEdit.setText(_translate("Dialog", "View Sorted groups"))
        self.Ignored.setText(_translate("Dialog", "Ignored URL/APPS List"))
        self.BlockedList.setText(_translate("Dialog", "Blocked List"))
        self.Title.setText(_translate("Dialog", "List of Opened Applications Today:"))
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date Opened"))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ignore? "))
        self.SaveButton.setText(_translate("Dialog", "Okay"))
        self.EditButton.setText(_translate("Dialog", "Edit"))
        self.SearchBar.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.GoButton.setText(_translate("Dialog", "Go!"))
        self.NumberEdit.setPlaceholderText(_translate("Dialog", "Set Entertainment Limit"))
        self.SETButton.setText(_translate("Dialog", "Ok"))
        self.RefreshButton.setText(_translate("Dialog", "Refresh"))
