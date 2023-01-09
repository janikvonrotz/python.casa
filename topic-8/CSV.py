import csv

with open('Mitarbeiter.csv', 'w') as file:

	# Um ein CSV zu schreiben, braucht es einen sogennanten Writer
    file_writer = csv.writer(file, delimiter=',', quotechar='"')

    # Die erste Zeile enthält die Tabellenüberschriften
    file_writer.writerow(['Name', 'Abteilung', 'Geboren im'])
    file_writer.writerow(['Peter Lustig', 'Buchhaltung', 'November'])
    file_writer.writerow(['Erika Meier', 'IT', 'März'])

with open('Mitarbeiter.csv', newline='') as file:

	# Dieses mal braucht es einen Reader
    file_reader = csv.reader(file, delimiter=',', quotechar='"')
    
    line_count = 0
    for row in file_reader:
    
        # Erste Zeile enthält Tabellenüberschriften
        if line_count == 0:
            print(f'Spaltennamen sind {", ".join(row)}')
        else:
            print(f'{row[0]} arbeitet in der Abteilung {row[1]} und ist geboren im {row[2]}.')
        line_count += 1
            
    print(f'{line_count} Zeilen wurden verarbeitet.')