# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\kille\Documents\Programming\Python\IA\UIs\AppModify.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AppName = QtWidgets.QLabel(self.centralwidget)
        self.AppName.setGeometry(QtCore.QRect(300, 20, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.AppName.setFont(font)
        self.AppName.setObjectName("AppName")
        self.LabelsList = QtWidgets.QTableWidget(self.centralwidget)
        self.LabelsList.setGeometry(QtCore.QRect(20, 160, 256, 411))
        self.LabelsList.setObjectName("LabelsList")
        self.LabelsList.setColumnCount(1)
        self.LabelsList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.LabelsList.setHorizontalHeaderItem(0, item)
        self.AddLabels = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLabels.setGeometry(QtCore.QRect(400, 230, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AddLabels.setFont(font)
        self.AddLabels.setText("")
        self.AddLabels.setObjectName("AddLabels")
        self.Entertainment = QtWidgets.QCheckBox(self.centralwidget)
        self.Entertainment.setGeometry(QtCore.QRect(470, 310, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Entertainment.setFont(font)
        self.Entertainment.setObjectName("Entertainment")
        self.Productivity = QtWidgets.QCheckBox(self.centralwidget)
        self.Productivity.setGeometry(QtCore.QRect(470, 370, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Productivity.setFont(font)
        self.Productivity.setObjectName("Productivity")
        self.Others = QtWidgets.QCheckBox(self.centralwidget)
        self.Others.setGeometry(QtCore.QRect(470, 430, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Others.setFont(font)
        self.Others.setObjectName("Others")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(640, 610, 111, 41))
        self.Save.setObjectName("Save")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(490, 610, 111, 41))
        self.Back.setObjectName("Back")
        self.Rename = QtWidgets.QLineEdit(self.centralwidget)
        self.Rename.setGeometry(QtCore.QRect(400, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Rename.setFont(font)
        self.Rename.setText("")
        self.Rename.setObjectName("Rename")
        self.Block = QtWidgets.QCheckBox(self.centralwidget)
        self.Block.setGeometry(QtCore.QRect(470, 490, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Block.setFont(font)
        self.Block.setObjectName("Block")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AppName.setText(_translate("MainWindow", "App Name"))
        item = self.LabelsList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Labels:"))
        self.AddLabels.setPlaceholderText(_translate("MainWindow", "Add Labels, Separate using comma"))
        self.Entertainment.setText(_translate("MainWindow", "Entertainment"))
        self.Productivity.setText(_translate("MainWindow", "Productivity"))
        self.Others.setText(_translate("MainWindow", "Others"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.Rename.setPlaceholderText(_translate("MainWindow", "Rename This App?"))
        self.Block.setText(_translate("MainWindow", "Block"))