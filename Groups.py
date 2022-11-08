from PyQt5 import QtCore, QtGui, QtWidgets
from UIs.ui_Groups import Ui_MainWindow

import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class GroupsCode(QtWidgets.QMainWindow):
    def __init__(self):
        super(GroupsCode, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Ent = self.ui.EntertainmentTable
        self.Prod = self.ui.ProductivityTable
        self.oth = self.ui.OtherTable

        self.Ent.setColumnWidth(0, 225)
        self.Prod.setColumnWidth(0, 225)
        self.oth.setColumnWidth(0, 225)

        self.ui.BackButton.clicked.connect(self.back)

        self.Entertainment()
        self.Productivity()
        self.Others()

    def back(self):
        # GoBack code
        from mainscreen import MainWindow
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    def Entertainment(self):
        query = "SELECT ALIAS FROM StoringData WHERE ENTERTAINMENT = ?"
        params = (1,)
        cursor.execute(query, params)
        results = cursor.fetchall()
        FinalResults = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])

        for i in FinalResults:
            self.AutoAddRows(FinalResults, self.Ent)

    def Productivity(self):
        query = "SELECT ALIAS FROM StoringData WHERE PRODUCTIVITY = ?"
        params = (1,)
        cursor.execute(query, params)
        results = cursor.fetchall()
        FinalResults = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])

        for i in FinalResults:
            self.AutoAddRows(FinalResults, self.Prod)

    def Others(self):
        query = "SELECT ALIAS FROM StoringData WHERE OTHER = ?"
        params = (1,)
        cursor.execute(query, params)
        results = cursor.fetchall()
        FinalResults = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])

        for i in FinalResults:
            self.AutoAddRows(FinalResults, self.oth)

    def AutoAddRows(self, results, table):

        FinalR = []

        for a in results:
            if a not in FinalR and a != "AdminAlias":
                FinalR.append(a)

        rowCounter = len(FinalR)
        # self.MainTable.setRowCount(0)
        table.setRowCount(rowCounter)

        tableindex = -1
        for row in FinalR:
            tableindex += 1
            table.setItem(
                tableindex, 0, QtWidgets.QTableWidgetItem(row))


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = GroupsCode()
    window.show()
    sys.exit(app.exec_())
