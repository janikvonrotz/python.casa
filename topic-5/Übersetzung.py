monate = {
    'january': 'Januar',
    'february': 'Feburar',
    'march': 'März',
    'april': 'April',
    'mai': 'Mai',
    'june': 'Juni',
    'july': 'Juli',
    'august': 'August',
    'september': 'September',
    'october': 'Oktober',
    'november': 'November',
    'december': 'Dezember'
}

# Lösung 1

for key, value in monate.items():
    print(f'The german translation for \'{value}\' is \'{value}\'')

# Lösung 2

for key in monate:
    print(f'The german translation for \'{key}\' is \'{monate[key]}\'')
