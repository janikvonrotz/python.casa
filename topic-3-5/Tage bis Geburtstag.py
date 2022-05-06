from datetime import datetime, date
geburtsdatum = input('Geben Sie ihr Geburtsdatum (DD.MM.YYYY) ein: ')
geburtsdatum = datetime.strptime(geburtsdatum, '%d.%m.%Y')

heute = date.today()
geburtstag = date(2022, geburtsdatum.month, geburtsdatum.day)

differenz = geburtstag - heute

print(f'Sie haben in {differenz.days} Tagen an einem {geburtstag.strftime("%A")} Geburtstag.')



