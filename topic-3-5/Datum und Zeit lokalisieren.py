import locale  
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')  # Linux    

from datetime import datetime
print(datetime.now().strftime('%A, %d. %B %Y'))