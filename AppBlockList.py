import subprocess
from datetime import datetime
import psutil
import os
import sqlite3
import difflib


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
                self.ActiveProcesses.append(line.decode('latin-1').rstrip())
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

            cursor.execute("SELECT APP FROM StoringData WHERE APP = ?", [i])

            res = cursor.fetchall()

            if not res:

                InsertInit = '''INSERT INTO StoringData(APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER,  BLOCKED, LABELS, ALIAS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                params = (i, 0, 0, 0, 0, 0, "None", i,  today)
                cursor.execute(InsertInit, params)
                conn.commit()

            else:
                cursor.execute(
                    "UPDATE StoringData SET Date_Open = ? WHERE APP = ?", (today, i))
                conn.commit()

    def killProcesses(self):
        cursor.execute("SELECT APP FROM StoringData WHERE BLOCKED = 1")
        results = cursor.fetchall()
        resultsFinal = []

        for i in range(len(results)):
            resultsFinal.append(results[i][0])

        for i in resultsFinal:
            for process in (process for process in psutil.process_iter() if process.name() == f"{i}.exe"):
                process.kill()


BlockList()
