import os, sys, sqlite3
if os.path.exists('lager.db'):
    os.remove('lager.db')
connection = sqlite3.connect('lager.db')
cursor = connection.cursor()
sql = """CREATE TABLE IF NOT EXISTS lager(
    id INTEGER PRIMARY KEY,
    name TEXT,
    referenz TEXT ,
    barcode TEXT,
    lager INTEGER,
    preis REAL)"""
cursor.execute(sql)
sql = "INSERT INTO lager VALUES(1, 'Holztisch', 'E-COM06', '601647855633', 3, 147)"
cursor.execute(sql)
sql = "INSERT INTO lager VALUES(2, 'Bürostuhl', 'E-COM06', '601647855634', 1, 70.50)"
cursor.execute(sql)
sql = "INSERT INTO lager VALUES(3, 'Abfalleimer', 'E-COM06', '601647855649', 5, 43)"
cursor.execute(sql)
connection.commit()
connection.close()