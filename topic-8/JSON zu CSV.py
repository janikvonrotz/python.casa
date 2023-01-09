import json
import csv
    
with open('people.json') as f:
    data = json.load(f)
print(data)

for person in data:
    print(f"name: {person['name']}")

with open('people.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"')

    # Erste Zeile enthält die Tabellenüberschriften
    csv_writer.writerow(['Name', 'Gender', 'Age'])
    for person in data:
        csv_writer.writerow(person.values())