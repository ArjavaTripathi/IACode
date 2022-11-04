from PyQt5 import QtCore, QtGui, QtWidgets
import configparser


configs = configparser.ConfigParser()


class verifyLogin():
    def __init__(self, user, passw):
        self.username = user
        self.password = passw

        # Add message to add password if first time open
        # Change all this to read from database instead
        if configs['Other']['firsttimeopen'] == "True":
            self.CreatePassword()

        else:
            self.verifyLoginFunc()

    def verifyLoginFunc(self):
        if self.password == configs['Password']['User1']:
            print("ENTER")  # Add popup dialog

        else:
            print("NO")

    def CreatePassword(self):

        configs.set('Password', 'User1', self.password)
        configs.set('Other', 'firsttimeopen', 'False')

        with open('info.ini', 'w') as configfile:
            configs.write(configfile)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 198)
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(200, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.PasswordInput = QtWidgets.QLineEdit(MainWindow)
        self.PasswordInput.setGeometry(QtCore.QRect(40, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setStyleSheet("border-color: rgb(170, 0, 0);")
        self.PasswordInput.setInputMask("")
        self.PasswordInput.setText("")
        self.PasswordInput.setMaxLength(32767)
        self.PasswordInput.setFrame(False)
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setCursorPosition(0)
        self.PasswordInput.setObjectName("PasswordInput")
        self.UserInput = QtWidgets.QLineEdit(MainWindow)
        self.UserInput.setGeometry(QtCore.QRect(40, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UserInput.setFont(font)
        self.UserInput.setWhatsThis("")
        self.UserInput.setStyleSheet("border-color: rgb(170, 0, 0);")
        self.UserInput.setInputMask("")
        self.UserInput.setText("")
        self.UserInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.UserInput.setObjectName("UserInput")
        self.LoginLabel = QtWidgets.QLabel(MainWindow)
        self.LoginLabel.setGeometry(QtCore.QRect(60, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setObjectName("LoginLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicked(self):
        username = self.UserInput.text()
        password = self.PasswordInput.text()
        verifyLogin(username, password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.PasswordInput.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.UserInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.LoginLabel.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
