#!/usr/bin/env python3
import json

# Klasse zur Speicherung eines Autors
class Author():
    def __init__(self, name):
        self.name = name
    
    # Objekt lesbar darstellen
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
        
# Klasse zur Speicherung eines Buchs
class Book():
    def __init__(self, title, isbn, authors):
        self.title = title
        self.isbn = isbn
        self.authors = authors
        
    # Objekt lesbar darstellen
    def __str__(self):
        allauth   = [ a.name for a in self.authors ]
        authnames = ', '.join(allauth)
        return '%s (ISBN %s): %s' % (self.title, self.isbn, authnames)
    def __repr__(self):
        # return 'Book(%s, %s, %d Authors)' % (self.title, self.isbn, len(self.authors))
        return self.__str__()

# eigener JSON-Encoder, der auch mit Author- und Book-Objekten zurecht kommt
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            # Buch als Dictionary darstellen, auch den Objekttyp speichern
            return {'_type_': 'Book', 'title': obj.title, 
                    'isbn': obj.isbn, 'authors': obj.authors}
        elif isinstance(obj, Author):
             # Autor als Dictionary darstellen
            return {'_type_': 'Author', 'name': obj.name}
        else:
            return json.JSONEncoder.default(self, obj)

# eigene JSON-Decoder, der auch mit Author- und Book-Objekten zurecht 
# kommt, wenn diese von MyEncoder codiert wurden
# Idee: https://gist.github.com/simonw/7000493
class MyDecoder(json.JSONDecoder):        
    # Konstruktur, erforderlich, damit der vordefinierte
    # JSONDecoder die eigene hook-Funktion verwendent
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, 
          object_hook=self.hook, *args, **kwargs)
    
    # eigener Decoder, berücksichtigt nur Objekte, die 
    # einen Dictionary-Eintrag der Form {'_type_': 'Book'}
    # oder {'_type_': 'Author'} aufweisen; alle anderen
    # Objekte unverändert weitergeben
    def hook(self, obj):
        if '_type_' not in obj:
            return obj
        type = obj['_type_']
        if type == 'Book':
            return Book(obj['title'], obj['isbn'], obj['authors'])
        elif type == 'Author':
            return Author(obj['name'])
        else:
            return obj

        
rapi = Book('Raspberry Pi', '978-3836265195', 
            [Author('Kofler'), Author('Scherbeck'), 
             Author('Kühnast')])

docker = Book('Docker', '978-3836261760',
              [Author('Öggl'), Author('Kofler')])

books = [rapi, docker]            

# books in JSON-Dokument umwandeln
s = json.dumps(books, cls=MyEncoder, ensure_ascii=False)

# aus dieser Zeichenkette wieder neue Objekte erzeugen
copy = json.loads(s, cls=MyDecoder)
print(copy)
