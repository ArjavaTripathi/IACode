import subprocess
from DatabaseStorage import DatabaseStorageClass
from datetime import date
import re


# Reformat database

class BlockList(DatabaseStorageClass):
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

        print(self.ActiveProcesses)  # StoreIntoDB


BlockList()
