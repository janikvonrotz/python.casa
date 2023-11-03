
a = 'abcde'
b = a
a = a + 'fg'
print(b)

from datetime import date
print(date.today())

from datetime import datetime
s = '2018-08-01 18:47'  
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')
print(dt.strftime('%H:%M'))

a = 'abcde'
print(a.upper())

text = "Der Film heisst \"Tenet\"."
print(text)
