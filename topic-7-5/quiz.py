import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()

# SQL-Abfrage mit Eingabe
frage = input("Bitte geben Sie eine Frage-ID ein: ")
sql = "SELECT * FROM questions WHERE questionID = " + frage

# SQL-Abfrage
# sql = "SELECT * FROM questions WHERE questionID = 403"

# Absenden der SQL-Abfrage und Empfang des Ergebnis
cursor.execute(sql)

# Ausgabe des Ergebnis
for datensatz in cursor:
    print("Frage: ", datensatz[1])
    print("Antworten: ", datensatz[2:6])

    korrekt = "1"
    antwort = "0"

    while korrekt != antwort:

        # Eingabe Antwort
        antwort = input("Ihre Antwort 1-4: ")

        # Ausgabe korrekt/falsch
        korrekt = str(datensatz[6])
        if korrekt == antwort:
            print("\nDie Antwort ist korrekt!\n")
        else:
            print("\nDie Antwort ist falsch!\n")

# Verbindung beenden
connection.close()