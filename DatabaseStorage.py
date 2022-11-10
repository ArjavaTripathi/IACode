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
                        ALIAS TEXT,
                        MAXEnt INTEGER,
                        DATE_OPEN TEXT
                    )''')

    def InsertIntoDatabase(self):

        InsertInit = '''INSERT INTO StoringData(Password, APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER, LABELS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?)'''
        #params = (APP, LABELS, IGNORED, DATE_OPEN)

        #self.cursor.execute(InsertInit, params)
        # self.conn.commit()


# DatabaseStorageClass()
today = datetime.today().strftime('%d-%m-%Y')

InsertInit = '''INSERT INTO StoringData(id, APP, IGNORED, ENTERTAINMENT, PRODUCTIVITY, OTHER,  BLOCKED, LABELS, ALIAS, DATE_OPEN) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
params = (1, "Admin", 1, 1, 1, 1, 1, "AdminLabel", "AdminAlias", today)
cursor.execute(InsertInit, params)
conn.commit()

#cursor.execute("DELETE FROM StoringData")
conn.commit()
