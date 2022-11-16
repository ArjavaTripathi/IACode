from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UIs.ui_IgnoreList import Ui_MainWindow

import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class IgnoreCode(QtWidgets.QMainWindow):
    def __init__(self):
        super(IgnoreCode, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Ignore.clicked.connect(self.ignorecode)

        self.ui.Unignore.clicked.connect(self.unignorecode)

        self.ui.BackButton.clicked.connect(self.Back)

    def Back(self):
        from mainscreen import MainWindow
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    def ignorecode(self):
        Name = self.ui.InputName.text()
        cursor.execute(
            "SELECT IGNORED FROM StoringData WHERE ALIAS = ?", [Name])
        results = cursor.fetchall()
        try:
            if results[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET IGNORED = 1 WHERE ALIAS = ?", [Name])
                conn.commit()
            elif results[0][0] == 1:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Already Ignored!")
                self.msg.setText(f"{Name} is already ignored!")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.show()
        except IndexError:
            self.msg2 = QMessageBox()
            self.msg2.setWindowTitle("Doesnt Exist!")
            self.msg2.setText(f"{Name} is not in Database!")
            self.msg2.setIcon(QMessageBox.Critical)
            self.msg2.show()

    def unignorecode(self):
        Name = self.ui.InputName.text()
        cursor.execute(
            "SELECT IGNORED FROM StoringData WHERE ALIAS = ?", [Name])
        results = cursor.fetchall()

        try:
            if results[0][0] == 1:
                cursor.execute(
                    "UPDATE StoringData SET IGNORED = 0 WHERE ALIAS = ?", [Name])
                conn.commit()
            elif results[0][0] == 0:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Already not ignored!")
                self.msg.setText(f"{Name} is already unignored!")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.show()
        except IndexError:
            self.msg2 = QMessageBox()
            self.msg2.setWindowTitle("Doesnt Exist!")
            self.msg2.setText(f"{Name} is not in Database!")
            self.msg2.setIcon(QMessageBox.Critical)
            self.msg2.show()


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = IgnoreCode()
    window.show()
    sys.exit(app.exec_())
