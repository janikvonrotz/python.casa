# Import Modul zum erstellen von Xlsx-Dateien
from xlsxwriter.workbook import Workbook
import sqlite3

def xlsx():
    # Datenbankverbindung wird hergestellt
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    
    # Alle Daten werden aus der Datenbank gelesen
    sql = "SELECT * FROM lager"
    cursor.execute(sql)
    data = cursor.fetchall()

    # Eine neue Excel-Datei wird erstellt
    workbook = Workbook('output.xlsx')
    # Neues Register definieren 
    worksheet = workbook.add_worksheet()
    # In der ersten Zeile sind die Tabellenüberschriften
    worksheet.write(0, 0, "ID")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "Referenz")
    worksheet.write(0, 3, "Barcode")
    worksheet.write(0, 4, "Lager")
    worksheet.write(0, 5, "Preis")

    # Schleife für jeden Datensatz aus der SQL-Abfrage
    for index, record in enumerate(data):
        # Beginned auf der zweite Zeile wird das Excel-Register geschrieben
        index = index+1
        # Schreibt den Inhalt des Datensatzes in die entsprechende Koordinate
        worksheet.write(index, 0, record[0])
        worksheet.write(index, 1, record[1])
        worksheet.write(index, 2, record[2])
        worksheet.write(index, 3, record[3])
        worksheet.write(index, 4, record[4])
        worksheet.write(index, 5, record[5])

    # Verbindung zur Datenbank wird geschlossen und Excel-Datei geschrieben
    connection.close()
    workbook.close()