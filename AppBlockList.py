import subprocess
from DatabaseStorage import DatabaseStorageClass
from datetime import date
import re


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

    """def editArray(self):

        del self.ActiveProcesses[0:3]

        for a in self.ActiveProcesses:  # Counts How Many Active Processes
            self.totalamount += 1

            today = str(date.today())  # Reformats Date
            retoday = re.sub("-", "/", today)
            self.ActiveProcesses.append(retoday)

            self.StoreIntoDB()

        print(self.ActiveProcesses)

    def StoreIntoDB(self):

        for a in self.ActiveProesses:  # Stores into database
            currentamount = 0
            while (currentamount < self.totalamount):
                param = (a, self.ActiveProesses[-1])
                DatabaseStorageClass().InsertIntoDatabase()

            currentamount += 1"""


BlockList()
