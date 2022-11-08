from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from UIs.ui_MainScreenUIDraft import Ui_Dialog
from datetime import datetime
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

        self.ui.SaveButton.clicked.connect(self.CheckIgnored)

        self.loaddata()

    def ViewGroups(self):
        from Groups import GroupsCode
        self.cams = GroupsCode()
        self.cams.show()
        self.close()

    def loaddata(self):
        today = datetime.today().strftime('%d-%m-%Y')
        params = [today]
        cursor.execute(
            "SELECT APP FROM StoringData WHERE DATE_OPEN = ?", [today])

        results = cursor.fetchall()
        FinalResults = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])
        print(FinalResults, " ", results)

        for i in FinalResults:
            self.AutoAddRows(FinalResults, today)

    def AutoAddRows(self, results, date):
        rowCounter = len(results)-1
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

        # Add Ignore and Block Code, then done!
        # try except case for None (AttributeError)
        try:
            # Write code to actually ignore the item!
            ItemtoIgnore = self.MainTable.item(cur, cur2-1).text()

            self.ui.IgnoredText.setText(f"{ItemtoIgnore} ignored")
        except AttributeError:
            self.ui.IgnoredText.setText("Select an item to ignore")


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
