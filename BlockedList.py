from PyQt5 import QtCore, QtGui, QtWidgets
from UIs.ui_BlockList import Ui_MainWindow

import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class BlockedCode(QtWidgets.QMainWindow):
    def __init__(self):
        super(BlockedCode, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Ta = self.ui.BlockList

        self.Ta.setColumnWidth(0, 254)

        self.ui.BackButton.clicked.connect(self.Back)

        self.LoadBlocked()

    def Back(self):
        from mainscreen import MainWindow
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    def LoadBlocked(self):
        cursor.execute(
            "SELECT APP FROM StoringData WHERE BLOCKED = ?", [1])

        results = cursor.fetchall()

        FinalResults = []

        for i in range(len(results)):
            FinalResults.append(results[i][0])

        for i in FinalResults:
            self.AutoAddRows(FinalResults)

    def AutoAddRows(self, results):

        rowCounter = len(results)

        self.Ta.setRowCount(rowCounter)

        tableindex = -1
        for row in results:
            tableindex += 1
            self.Ta.setItem(
                tableindex, 0, QtWidgets.QTableWidgetItem(row))


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = BlockedCode()
    window.show()
    sys.exit(app.exec_())
