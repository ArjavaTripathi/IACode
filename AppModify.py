from PyQt5 import QtCore, QtGui, QtWidgets
from UIs.ui_AppModify import Ui_MainWindow
import re
import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class ModifyCode(QtWidgets.QMainWindow):
    def __init__(self, Name):
        super(ModifyCode, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name = Name

        self.ui.AppName.setText(self.name)

        self.ui.LabelsList.setColumnWidth(0, 254)

        self.ui.Save.clicked.connect(self.SaveCode)

        self.fillTable()

    def fillTable(self):

        query = "SELECT LABELS FROM StoringData WHERE APP = ?"
        params = (self.name,)
        cursor.execute(query, params)
        results = cursor.fetchall()
        finalR = []
        if results[0][0] != None:
            for i in range(len(results)):
                x = re.split(",", results[i][0])
                print(x)

            rowCounter = len(x)
            # self.MainTable.setRowCount(0)
            self.ui.LabelsList.setRowCount(rowCounter)

            tableindex = -1
            for row in x:
                tableindex += 1
                self.ui.LabelsList.setItem(
                    tableindex, 0, QtWidgets.QTableWidgetItem(row))

    def SaveCode(self):
        NewLabel = self.ui.AddLabels.text()

        if NewLabel != "":
            cursor.execute("UPDATE StoringData SET LABELS = ? WHERE APP = ?", [
                           NewLabel, self.name])
            conn.commit()


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ModifyCode()
    window.show()
    sys.exit(app.exec_())
