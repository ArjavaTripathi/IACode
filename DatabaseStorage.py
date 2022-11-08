import sqlite3
from datetime import datetime

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


class DatabaseStorageClass:
    def __init__(self):
        self.makeDatabase()

    def makeDatabase(self):

        cursor.execute('''CREATE TABLE IF NOT EXISTS StoringData(
                        id PRIMARY KEY,
                        Password Text,
                        APP TEXT not null,
                        IGNORED BIT NOT NULL,
                        ENTERTAINMENT BIT NOT NULL,
                        PRODUCTIVITY BIT NOT NULL,
                        OTHER BIT NOT NULL,
                        BLOCKED BUT NOT NULL,
                        LABELS TEXT,
                        DATE_OPEN TEXT
                    )''')

    def InsertIntoDatabase(self):

        InsertInit = '''INSERT INTO StoringData(Password, APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER, LABELS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?)'''
        #params = (APP, LABELS, IGNORED, DATE_OPEN)

        #self.cursor.execute(InsertInit, params)
        # self.conn.commit()


# DatabaseStorageClass()
today = datetime.today().strftime('%d-%m-%Y')
print(today)
print()

InsertInit = '''INSERT INTO StoringData(id, APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER,  BLOCKED, LABELS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'''
params = (200, "5050", 0, 0, 0, 0, 0, "Communication, Results", today)
cursor.execute(InsertInit, params)
conn.commit()
