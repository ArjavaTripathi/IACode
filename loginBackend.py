
from PyQt5 import QtCore, QtGui, QtWidgets
from UIs.ui_LoginUI import Ui_MainWindow

import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class LoginCode(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginCode, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.clicked)

    def clicked(self):
        username = self.ui.UserInput.text()
        password = self.ui.PasswordInput.text()

        usernameCorr = "Admin"

        cursor.execute(
            '''SELECT Password FROM StoringData WHERE id = ?''', [1])

        passwordCorr = cursor.fetchall()

        print(passwordCorr)

        if username == usernameCorr and password == passwordCorr[0][0]:
            print("Success!")  # NextSlide
            from mainscreen import MainWindow
            self.cams = MainWindow()
            self.cams.show()
            self.close()
        else:

            if passwordCorr[0][0] == "":
                cursor.execute(
                    '''UPDATE StoringData SET password = ? WHERE id = ?''', [password, 1])  # Doesnt Work!

                conn.commit()

            else:
                self.ui.LoginLabel.setText("Login Failed!")


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginCode()
    window.show()
    sys.exit(app.exec_())
