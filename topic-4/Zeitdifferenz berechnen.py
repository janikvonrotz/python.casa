from datetime import date, timedelta  
today = date.today()  
weihnachten = date(today.year, 12, 24)  
warten = weihnachten - today  
print('Noch', warten.days, 'Tage bis Weihnachten.')