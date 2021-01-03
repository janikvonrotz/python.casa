#!/usr/bin/env python3
import json

with open('sample.json', 'r') as f:
    data = json.load(f)
    
print('data:', data)

for book in data:
    print('Titel:   ', book['title'])
    print('ISBN:    ', book['isbn'])
    print('Autoren: ', ', '.join(book['authors']))
    print()


lst1 = list(range(1, 5))
lst2 = list(range(10, 15))
dict = {'name': 'abc äöü', 'list1': lst1, 'list2': lst2}
print(json.dumps(dict))
print(json.dumps(dict, indent=2, ensure_ascii=False))

