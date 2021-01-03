#!/usr/bin/env python3
import json
import urllib.request
# bitte besorgen Sie sich auf 
# https://developer.nytimes.com/signup einen
# eigenen Key!
url      = 'https://api.nytimes.com/svc/books/v3/lists.json?api-key=3cd817e0eb0a4f74823abe6337def4fa&list=hardcover-fiction'
response = urllib.request.urlopen(url)
binary   = response.read()        # binäre Daten
txt      = binary.decode('utf-8') # als Text interpretieren
top15    = json.loads(txt)

for result in top15['results']:
    detail = result['book_details'][0]
    print('Titel:', detail['title'])
    print('Autor:', detail['author'])
    print('ISBN: ', detail['primary_isbn13'])
    print()

