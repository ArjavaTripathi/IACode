import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

usernameindatabase = "whatever"
passwordindatabase = "whatever2"

LoginStatus = False


class LoginPage(QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Login')
        self.resize(350, 200)

        UsernameLabel = QtWidgets.QLabel()
        UsernameLabel.setText("Username")
        UsernameLabel.move(50, 50)


app = QApplication(sys.argv)
form = LoginPage()
form.show()
sys.exit(app.exec_())
