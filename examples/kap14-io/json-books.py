#!/usr/bin/env python3
import json

class Author():
    def __init__(self, name):
        self.name = name
        
class Book():
    def __init__(self, title, isbn, authors):
        self.title = title
        self.isbn = isbn
        self.authors = authors

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {'title': obj.title, 'isbn': obj.isbn, 'authors': obj.authors}
        elif isinstance(obj, Author):
            return obj.name
        else:
            return json.JSONEncoder.default(self, obj)
        
rapi = Book('Raspberry Pi', '978-3836265195', 
            [Author('Kofler'), Author('Scherbeck'), 
             Author('Kühnast')])

docker = Book('Docker', '978-3836261760',
              [Author('Öggl'), Author('Kofler')])

books = [rapi, docker]            

# books in der Datei sample.json speichern
with open('sample.json', 'w') as f:
    json.dump(books, f, cls=MyEncoder, 
              ensure_ascii=False, indent=4)
