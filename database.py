import sqlite3

conn = sqlite3.connect('portfolio.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    message TEXT
)
''')

conn.commit()
conn.close()