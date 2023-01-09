import json
with open('Bücher.json') as f:
    data = json.load(f)
print(data)

for book in data:
    print(f"Titel: {book['title']}")
    for author in book['authors']:
        print(f"Author: {author}")
    print('')