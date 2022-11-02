import sqlite3

conn = sqlite3.connect('processes.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS StoringData(
                APP TEXT,
                DATE_OPEN TEXT
            )''')

InsertInit = '''INSERT INTO StoringData(APP, DATE_OPEN) VALUES(?,?)'''