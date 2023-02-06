import sqlite3
connection = sqlite3.connect('lager.db')
sql = """CREATE TABLE lager(
    id INTEGER PRIMARY KEY,
    name TEXT,
    referenz TEXT,
    barcode TEXT,
    lager INTEGER,
    preis REAL)"""
connection.execute(sql)
connection.close()