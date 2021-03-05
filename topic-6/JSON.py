import json
with open('Bücher.json', 'r') as f:
    data = json.load(f)
print(data)

for book in data:
    print(f"Titel: {book['title']}")
    for author in book['authors']:
        print(f"Author: {author}")
    print('')