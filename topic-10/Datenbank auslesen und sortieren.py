import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM questions WHERE questionID = 403"

# Absenden der SQL-Abfrage und Empfang des Ergebnis
cursor.execute(sql)

# Ausgabe des Ergebnis
for datensatz in cursor:
    print("Frage: ", datensatz[1])
    print("Antworten: ", ', '.join(datensatz[2:6]))

# Verbindung beenden
connection.close()