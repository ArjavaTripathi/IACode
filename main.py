import tkinter
import sqlite3 
import pandas as pd

conn = sqlite3.connect('email.db')
cursor = conn.cursor()

password = "1"

cursor.execute('''CREATE TABLE IF NOT EXISTS Data(
                id INTEGER PRIMARY KEY, 
                FIRST_NAME TEXT NOT NULL,
                LAST_NAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL
            )''')

class DataEntry:
    def __init__(self, FirstName, LastName, Email):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email 
    def AddData(self, FirstName, LastName, Email): 
        
        InitInsert = '''INSERT INTO Data(First_Name, Last_Name, Email) VALUES(?,?,?)'''
        param = (FirstName, LastName, Email)
        cursor.execute(InitInsert, param)
        conn.commit()

    def ViewData(self): 
        print(pd.read_sql_query("SELECT * FROM Data", conn))
    
    def DeleteData(self, FirstNameDelete, LastNameDelete, EmailDelete):
        deletesql = '''DELETE from Data where First_Name = (?), Last_Name = (?), Email = (?);'''
        param = (FirstNameDelete, LastNameDelete, EmailDelete)

        cursor.execute(deletesql, param)
        conn.commit()

        DataEntry(FirstName = None, LastName = None, Email = None).ViewData()
        


def StripName(Name, Email): 
    FirstName = Name.split()[0]
    LastName = Name.split()[1]
    
    DataEntry(FirstName, LastName, Email).AddData(FirstName, LastName, Email)

Log = str(input("Enter the password: "))

if Log == password: 
    print("Login Successful")
    NextAction = str(input("What would you like to do? "))
    if NextAction == "Add":
        Name = str(input("Enter your full name: "))
        Email = str(input("Enter your email address: "))
        StripName(Name, Email)
    elif NextAction == "View": 
        DataEntry(FirstName = None , LastName = None, Email = None).ViewData()
    elif NextAction == "Delete": 
        WhichDelete = str(input("Enter the full name and email of user you want to delete: "))

        FirstNameDelete = WhichDelete.split()[0]
        LastNameDelete = WhichDelete.split()[1]
        EmailDelete = WhichDelete.split()[2]

        DataEntry(FirstName = None, LastName = None, Email = None).DeleteData(FirstNameDelete, LastNameDelete, EmailDelete)
else:
    print("Login Failed")
    