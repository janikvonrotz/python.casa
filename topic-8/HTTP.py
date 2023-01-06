import urllib.request

# HTTP-Request ausführen
url = 'http://example.com'
response = urllib.request.urlopen(url)
binary = response.read() # Download durchführen
html = binary.decode('utf-8') # Dokument muss decodiert werden

with open('index.html', 'wt') as file:
    file.write(html)