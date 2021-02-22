key = "Blau"
value = '#FFFF00'
d = {'Rot': '#FF0000', key: '#0000FF', "Gelb": value}
print(d)

print(d.get('Gelb')) # Ausgabe: #FFFF00
print(d.values()) # dict_values(['#FF0000', '#0000FF', '#FFFF00'])
print(d.keys()) # dict_keys(['Rot', 'Blau', 'Gelb'])