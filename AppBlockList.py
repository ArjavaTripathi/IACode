import subprocess
from DatabaseStorage import *
from datetime import date 
import re

ActiveProcesses = []
StoreProcesses = []

totalamount = 0

def getProcess():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            # only print lines that are not empty
            # decode() is necessary to get rid of the binary string (b')
            # rstrip() to remove `\r\n`
            print(line.decode().rstrip())
            ActiveProcesses.append(line.decode().rstrip())


getProcess()

del ActiveProcesses[0:3]




for a in ActiveProcesses:   #Adds to StoreProcesses
    StoreProcesses.append(a)
    totalamount += 1 

today = str(date.today())   #Reformats Date
retoday = re.sub("-", "/", today)
StoreProcesses.append(retoday)



for a in StoreProcesses:    #Stores into database
    currentamount = 0
    while(currentamount < totalamount):
        param = (a, StoreProcesses[-1])
        cursor.execute(InsertInit, param)




