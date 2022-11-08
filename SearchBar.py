from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UIs.ui_SearchBar import Ui_MainWindow
from datetime import datetime

import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class SearchBarCode(QtWidgets.QMainWindow):
    def __init__(self, searchQuery):
        super(SearchBarCode, self).__init__()

        self.searchQuery = searchQuery[0]

        self.Group = False

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnCount(1)

        self.ui.tableWidget.setColumnWidth(0, 550)

        self.autocompletetable()

        self.ui.BackButton.clicked.connect(self.back)

        self.ui.BackButton_2.clicked.connect(self.Match)

    def autocompletetable(self):
        today = datetime.today().strftime('%d-%m-%Y')
        try:
            cursor.execute(
                "SELECT {} FROM StoringData".format(self.searchQuery))

            self.Group = True

            results = cursor.fetchall()
            final = []
            final.append(self.searchQuery)

            self.AddRows(final)

        except:
            cursor.execute("SELECT APP FROM StoringData WHERE ALIAS = ? AND DATE_OPEN = ?", (
                           self.searchQuery, today))
            results = cursor.fetchall()
            results = list(results)

            if len(results) == 0:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Nothing Found!")
                self.msg.setText(
                    "Nothing Found! Make sure you are using the renamed name instead of the full name if one was set, and group names should be in all caps!")
                self.msg.show()
            else:
                final = []
                for i in range(len(results)):
                    final.append(results[i][0])

                self.AddRows(final)

    def AddRows(self, FinalR):
        rowCounter = len(FinalR)
        self.ui.tableWidget.setRowCount(rowCounter)

        tableindex = -1
        for row in FinalR:
            tableindex += 1
            self.ui.tableWidget.setItem(
                tableindex, 0, QtWidgets.QTableWidgetItem(row))

    def back(self):
        from mainscreen import MainWindow
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    def Match(self):
        cur = self.ui.tableWidget.currentRow()

        if self.Group == True:
            from Groups import GroupsCode
            self.cams = GroupsCode()
            self.cams.show()
            self.close()
        else:
            from AppModify import ModifyCode
            wheretogo = self.ui.tableWidget.item(cur, 0).text()

            self.cams = ModifyCode(wheretogo)
            self.cams.show()
            self.close()


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SearchBarCode()
    window.show()
    sys.exit(app.exec_())
