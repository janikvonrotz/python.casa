from datetime import datetime, date
geburtsdatum = input('Geben Sie ihr Geburtsdatum (DD.MM.YYYY) ein: ')
geburtsdatum = datetime.strptime(geburtsdatum, '%d.%m.%Y')
heute = date.today()

differenz = date.today() - geburtsdatum.date()

print(f'Seit meiner Geburt sind {differenz.days} Tage vergangen')


