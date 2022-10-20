
from xlsxwriter.workbook import Workbook
import sqlite3

def xlsx():
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM lager"
    cursor.execute(sql)
    data = cursor.fetchall()

    workbook = Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "ID")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "Referenz")
    worksheet.write(0, 3, "Barcode")
    worksheet.write(0, 4, "Lager")
    worksheet.write(0, 5, "Preis")

    for index,record in enumerate(data):
        index = index+1
        worksheet.write(index, 0, record[0])
        worksheet.write(index, 1, record[1])
        worksheet.write(index, 2, record[2])
        worksheet.write(index, 3, record[3])
        worksheet.write(index, 4, record[4])
        worksheet.write(index, 5, record[5])

    connection.close()
    workbook.close()