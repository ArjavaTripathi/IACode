import subprocess
from datetime import datetime
import re
import sqlite3


conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class BlockList():
    def __init__(self):
        self.ActiveProcesses = []
        self.getProcess()

    def getProcess(self):  # Getting open processes
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line.rstrip():
                # only print lines that are not empty
                # decode() is necessary to get rid of the binary string (b')
                # rstrip() to remove `\r\n`
                # print(line.decode().rstrip())
                self.ActiveProcesses.append(line.decode().rstrip())
                #
                #
                # self.editArray()

        try:
            self.ActiveProcesses.remove('-----------')
            self.ActiveProcesses.remove('Description')
            self.ActiveProcesses.remove('Application Frame Host')
        except ValueError:
            pass

        for i in self.ActiveProcesses:
            today = datetime.today().strftime('%d-%m-%Y')
            InsertInit = '''INSERT INTO StoringData(APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER,  BLOCKED, LABELS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
            params = (i, 0, 0, 0, 0, 0, "None",  today)
            cursor.execute(InsertInit, params)
            conn.commit()


BlockList()
