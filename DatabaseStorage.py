import sqlite3


class DatabaseStorageClass:
    def __init__(self):
        self.conn = sqlite3.connect('processes.db')
        self.cursor = self.conn.cursor()

    def makeDatabase(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS StoringData(
                        APP TEXT not null,
                        LABELS TEXT,
                        IGNORED BIT NOT NULL,
                        DATE_OPEN TEXT
                    )''')

    def InsertIntoDatabase(self):

        InsertInit = '''INSERT INTO StoringData(APP, DATE_OPEN) VALUES(?,?)'''
        #params = (APP, LABELS, IGNORED, DATE_OPEN)

        #self.cursor.execute(InsertInit, params)
        # self.conn.commit()
