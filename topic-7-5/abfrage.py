import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("lager.db")
cursor = connection.cursor()

# Datensatz aktualisieren
sql = "UPDATE lager SET preis = 71 WHERE id = 2"
cursor.execute(sql)
connection.commit()

# Datensatz löschen
sql = "DELETE FROM lager WHERE id = 3"
cursor.execute(sql)
connection.commit()

# SQL-Abfrage
sql = "SELECT * FROM lager"

# Absenden der SQL-Abfrage und Empfang des Ergebnis
cursor.execute(sql)

# Ausgabe des Ergebnis
for datensatz in cursor:
    print(datensatz[1])
    print(datensatz)

# Verbindung beenden
connection.close()