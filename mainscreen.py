from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from UIs.ui_MainScreenUIDraft import Ui_Dialog
from datetime import datetime
from AppBlockList import BlockList
import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ViewAndEdit.clicked.connect(self.ViewGroups)

        # self.ui.Ignored.clicked.connect()

        # self.ui.BlockedList.clicked.connect()

        self.MainTable = self.ui.MainTable
        self.MainTable.setColumnWidth(0, 100)
        self.MainTable.setColumnWidth(1, 200)

        self.ui.EditButton.clicked.connect(self.EditPage)
        self.ui.SaveButton.clicked.connect(self.CheckIgnored)
        self.ui.Ignored.clicked.connect(self.IgnoredButton)
        self.ui.BlockedList.clicked.connect(self.BlockedRedirect)
        self.ui.GoButton.clicked.connect(self.go)
        self.ui.SETButton.clicked.connect(self.setmax)
        BlockList()
        self.loaddata()

    def IgnoredButton(self):
        from IgnoreList import IgnoreCode
        self.cams = IgnoreCode()
        self.cams.show()
        self.close()

    def BlockedRedirect(self):
        from BlockedList import BlockedCode
        self.cams = BlockedCode()
        self.cams.show()
        self.close()

    def ViewGroups(self):
        from Groups import GroupsCode
        self.cams = GroupsCode()
        self.cams.show()
        self.close()

    def loaddata(self):
        today = datetime.today().strftime('%d-%m-%Y')
        params = [today]
        cursor.execute(
            "SELECT ALIAS FROM StoringData WHERE DATE_OPEN = ?", [today])

        results = cursor.fetchall()
        FinalResults = []
        FinalR = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])

        print(FinalResults, " Before")

        for i in FinalResults:
            cursor.execute(
                "SELECT IGNORED FROM StoringData WHERE ALIAS = ?", [i])
            r = cursor.fetchall()
            if r[0][0] == 1:
                FinalResults.remove(i)

        print(FinalResults, " After")

        for i in FinalResults:
            self.AutoAddRows(FinalResults, today)

    def AutoAddRows(self, results, date):
        rowCounter = len(results)
        # self.MainTable.setRowCount(0)
        self.MainTable.setRowCount(rowCounter)
        tableindex = -1

        AlreadyIn = []

        for row in results:
            if row not in AlreadyIn:
                tableindex += 1
                self.MainTable.setItem(
                    tableindex, 1, QtWidgets.QTableWidgetItem(row))
                self.MainTable.setItem(
                    tableindex, 0, QtWidgets.QTableWidgetItem(date))

                AlreadyIn.append(row)

    def CheckIgnored(self):
        cur = self.MainTable.currentRow()
        cur2 = self.MainTable.currentColumn()

        ItemtoIgnore = self.MainTable.item(cur, cur2-1).text()

        cursor.execute(
            "SELECT IGNORED FROM StoringData WHERE ALIAS = ?", [ItemtoIgnore])

        results = cursor.fetchall()
        try:
            if results[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET IGNORED = 1 WHERE ALIAS = ?", [ItemtoIgnore])
                conn.commit()
                self.msg0 = QMessageBox()
                self.msg0.setWindowTitle("Ignored!")
                self.msg0.setText(f"{ItemtoIgnore} is now ignored!")
                self.msg0.setIcon(QMessageBox.Information)
                self.msg0.show()
            elif results[0][0] == 1:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Already Ignored!")
                self.msg.setText(f"{ItemtoIgnore} is already ignored!")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.show()
        except:
            self.msg2 = QMessageBox()
            self.msg2.setWindowTitle("Doesnt Exist!")
            self.msg2.setText(f"{ItemtoIgnore} is not in Database!")
            self.msg2.setIcon(QMessageBox.Critical)
            self.msg2.show()

            self.ui.IgnoredText.setText(f"{ItemtoIgnore} ignored")

    def EditPage(self):
        from AppModify import ModifyCode
        try:
            cur = self.MainTable.currentRow()
            cur2 = self.MainTable.currentColumn()
            ItemtoIgnore = self.MainTable.item(cur, cur2).text()
            self.cams = ModifyCode(ItemtoIgnore)
            self.cams.show()
            self.close()
        except AttributeError:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Error!")
            self.msg.setText("Please first click on an App Name!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.show()

    def go(self):
        from SearchBar import SearchBarCode
        Name = self.ui.SearchBar.text()

        print(Name)

        self.cams = SearchBarCode([Name])
        self.cams.show()
        self.close()

    def setmax(self):
        MaxNo = self.ui.NumberEdit.text()

        try:
            Max = int(MaxNo)

            cursor.execute(
                "UPDATE StoringData SET MAXEnt = ? WHERE id = 1", (Max,))
            conn.commit()
        except ValueError:
            self.msgVal = QMessageBox()
            self.msgVal.setWindowTitle("Incorrect Format!")
            self.msgVal.setText(
                "Please Enter a Number for the maximum number of entertainment applications allowed today!")
            self.msgVal.setIcon(QMessageBox.Information)
            self.msgVal.show()


if __name__ == '__main_':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
