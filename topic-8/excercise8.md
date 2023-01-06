# Übungen Thema 8

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 8.1: Fehler abfangen

### Aufgabe 8.2: Fehler Datentyp behandeln

Angenommen Sie haben diese Python-Funktion.

```python
def pluszwei(zahl):
	return (zahl + 2)
```

Und verwenden Sie in ihrem Programm.

```python
print(pluszwei(2))
print(pluszwei('3'))
```

Bei der Ausführung erhalten Sie einen Fehler vom Typ `TypeError`. Fangen Sie diesen Fehler in ihrem Programm mithilfe von `try` and `except` ab.

### Aufgabe 8.3: Datei lesen und schreiben

### Aufgabe 8.4: JSON to CSV konvertieren

Sie erhalten das folgende JSON-Dokument `people.json`:

```json
[
    {
        "name": "Jason",
        "gender": "M",
        "age": 27
    },
    {
        "name": "Rosita",
        "gender": "F",
        "age": 23
    },
    {
        "name": "Leo",
        "gender": "M",
        "age": 19
    }
]
```

Damit Sie es verarbeiten können brauche Sie es im CSV-Format.

Entwickeln Sie ein Programm, dass dieses JSON-Dokuments zu einem CSV konvertiert.

Dazu diese Inputs:

```python
import json
import csv
```

```python
with open('people.json', 'r') as f:
    data = json.load(f)
print(data)
```

```python
for person in data:
    print(f"name: {person['name']}")
```

```python
with open('people.csv', mode='w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"')
```

```python
    csv_writer.writerow(['Name', 'Gender', 'Age'])
    for person in data:
        csv_writer.writerow(person.values())
```

### Aufgabe 8.5: Erste Website

Erstellen Sie eine persönliche Website mit einem HTML-Dokument. Nennen Sie das Dokument `mypage.html`.

Fügen Sie in der Website mithilfe des `<pre>` HTML-Tag Python-Code ein.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Python-Code in HTML</title>
</head>
<body>
  <h2>Python-Code in HTML</h2>
  <pre>
with open('people.json', 'r') as f:
	data = json.load(f)
print(data)
  </pre>
</body>
</html>
```

### Aufgabe 8.6: Dynamische Website

### Aufgabe 8.7: Webserver

Die erstellte Website wollen wir nun publizieren. Dazu erstellen wir einen HTTP-Server. Dieser lädt unsere Website und stellt Sie für andere Computer bereit.

Führen Sie das folgende Programm `Server.py` aus.

```python
import http.server
import socketserver

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mypage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Erstelle ein Objekt anhand der obigen Klasse
handler = HttpRequestHandler

server = socketserver.TCPServer(("", 8000), handler)

# Starte den Server
server.serve_forever()
```

Und öffnen Sie diesen Link <http://localhost:8000/>.

In der Python-Konsole sehen Sie nun die Website-Aufrufe.

Nun möchten wir das Programm anpassen. Ändern Sie den Port von `8000` auf den HTTP-Standardport `80` und zeigen Sie die Website unter der richtigen Adresse an.

::: warning
Falls Sie beim Starten des Webservers aufgrund der Portänderung einen Fehler erhalten, belassen Sie den Port bei `8000`
:::

### Aufgabe 8.8: Intranet

Wenn ihr Computer und der ihrer Nachbaren im selben WLAN bzw. Netzwerk sind, sind die Voraussetzungen für ein Intranet gegeben.

Haben ihre Nachbaren die Website gestartet können Sie anhand der IP-Adresse darauf zugreifen.

Zeigen Sie ihre lokale IPv4-Adresse über die Netzwerkeinstellungen des Computers an. Dazu ein Beispiel wie das auf einem Linux-Computer aussieht:

![](../linux-ipv4.png)

Tauschen Sie die IP-Adresse mit ihrem Nachbarn aus und rufen Sie die Website im Browser damit auf. Beispiel: <http://192.168.1.104:8000>.
