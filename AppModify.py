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

        self.ui.Back.clicked.connect(self.BackButton)

        cursor.execute(
            "SELECT ENTERTAINMENT FROM StoringData WHERE ALIAS = ?", [self.name])

        resEnt = cursor.fetchall()

        if resEnt[0][0] == 1:
            self.ui.Entertainment.setChecked(True)

        cursor.execute(
            "SELECT PRODUCTIVITY FROM StoringData WHERE ALIAS = ?", [self.name])

        resProd = cursor.fetchall()

        if resProd[0][0] == 1:
            self.ui.Productivity.setChecked(True)

        cursor.execute(
            "SELECT OTHER FROM StoringData WHERE ALIAS = ?", [self.name])

        resOth = cursor.fetchall()

        if resOth[0][0] == 1:
            self.ui.Others.setChecked(True)

        cursor.execute(
            "SELECT BLOCKED FROM StoringData WHERE ALIAS = ?", [self.name])

        resBlo = cursor.fetchall()

        if resBlo[0][0] == 1:
            self.ui.Block.setChecked(True)

        self.fillTable()

    def fillTable(self):

        query = "SELECT LABELS FROM StoringData WHERE ALIAS = ?"
        params = (self.name,)
        cursor.execute(query, params)
        results = cursor.fetchall()

        finalR = []
        if results[0][0] != None:
            for i in range(len(results)):
                x = re.split(",", results[i][0])

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
        Alias = self.ui.Rename.text()
        EntertainmentCheck = self.ui.Entertainment
        ProductivityCheck = self.ui.Productivity
        OthersCheck = self.ui.Others
        BlockedCheck = self.ui.Block

        if NewLabel != "":
            print("Running")
            cursor.execute("UPDATE StoringData SET LABELS = ? WHERE ALIAS = ?", [
                           NewLabel, self.name])
            conn.commit()
        if Alias != "":
            cursor.execute(
                "SELECT APP FROM StoringData WHERE ALIAS = ?", [self.name])
            resultsname = cursor.fetchall()
            cursor.execute("UPDATE StoringData SET ALIAS = ? WHERE APP = ?", [
                           Alias, resultsname[0][0]])
            conn.commit()

        if EntertainmentCheck.isChecked():
            cursor.execute(
                "SELECT ENTERTAINMENT FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()

            if resent[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET ENTERTAINMENT = ? WHERE ALIAS = ?", [1, self.name])
                conn.commit()
        else:
            cursor.execute(
                "SELECT ENTERTAINMENT FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()
            if resent[0][0] == 1:
                cursor.execute(
                    "UPDATE StoringData SET ENTERTAINMENT = ? WHERE ALIAS = ?", [0, self.name])
                conn.commit()

        if ProductivityCheck.isChecked():
            cursor.execute(
                "SELECT PRODUCTIVITY FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()

            if resent[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET PRODUCTIVITY = ? WHERE ALIAS = ?", [1, self.name])
                conn.commit()
        else:
            cursor.execute(
                "SELECT PRODUCTIVITY FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()
            if resent[0][0] == 1:
                cursor.execute(
                    "UPDATE StoringData SET PRODUCTIVITY = ? WHERE ALIAS = ?", [0, self.name])
                conn.commit()

        if OthersCheck.isChecked():
            cursor.execute(
                "SELECT OTHER FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()

            if resent[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET OTHER = ? WHERE ALIAS = ?", [1, self.name])
                conn.commit()
        else:
            cursor.execute(
                "SELECT OTHER FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()
            if resent[0][0] == 1:
                cursor.execute(
                    "UPDATE StoringData SET OTHER = ? WHERE ALIAS = ?", [0, self.name])
                conn.commit()

        if BlockedCheck.isChecked():
            cursor.execute(
                "SELECT BLOCKED FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()

            if resent[0][0] == 0:
                cursor.execute(
                    "UPDATE StoringData SET BLOCKED = ? WHERE ALIAS = ?", [1, self.name])
                conn.commit()
        else:
            cursor.execute(
                "SELECT BLOCKED FROM StoringData WHERE ALIAS = ?", [self.name])
            resent = cursor.fetchall()
            if resent[0][0] == 1:
                cursor.execute(
                    "UPDATE StoringData SET BLOCKED = ? WHERE ALIAS = ?", [0, self.name])
                conn.commit()

    def BackButton(self):
        print("Hi")
        from mainscreen import MainWindow
        self.cams = MainWindow()
        self.cams.show()
        self.close()


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ModifyCode()
    window.show()
    sys.exit(app.exec_())
