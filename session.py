import sqlite3


db = sqlite3.connect('database.sqlite3')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users bla bla bla")  # Linguagem SQL
