# Übungen Thema 6

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 6.1: Fehler abfangen

Angenommen sie erhalten diese Python-Funktion.

```py
def pluszwei(zahl):
	return (zahl + 2)
```

Und verwenden sie in ihrem Programm.

```py
print(pluszwei(2))
print(pluszwei('3'))
```

Bei der Ausführung erhalten sie einen Fehler vom Typ `TypeError`. Fangen sie diesen Fehler in ihrem Programm mithilfe von `try` and `except` ab.

### Aufgabe 6.2: JSON to CSV konvertieren

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

Damit sie es verarbeiten können brauche sie es im CSV-Format.

Entwickeln sie ein Programm, dass dieses JSON-Dokuments zu einem CSV konvertiert.

Dazu diese Inputs:

```py
import json
import csv
```

```py
with open('people.json', 'r') as f:
    data = json.load(f)
print(data)
```

```py
for person in data:
    print(f"name: {person['name']}")
```

```py
with open('people.csv', mode='w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"')
```

```py
    csv_writer.writerow(['Name', 'Gender', 'Age'])
    for person in data:
        csv_writer.writerow(person.values())
```

### Aufgabe 6.3: Erste Website

Erstellen sie eine persönliche Website mit einem HTML-Dokument. Nennen sie das Dokument `mypage.html`.

Fügen sie in der Website mithilfe des `<pre>` HTML-Tag Python-Code ein.

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

### Aufgabe 6.4: Webserver

Die erstellte Website wollen wir nun publizieren. Dazu erstellen wir einen HTTP-Server. Dieser lädt unsere Website und stellt sie für andere Computer bereit.

Führen sie das folgende Programm `Server.py` aus.

```py
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

Und öffnen sie diesen Link <http://localhost:8000/>.

In der Python-Konsole sehen sie nun die Website-Aufrufe.

Nun möchten wir das Programm anpassen. Ändern sie den Port von `8000` auf den HTTP-Standardport `80` und zeigen sie die Website unter der richtigen Adresse an.

::: warning
Falls sie beim Starten des Webservers aufgrund der Portänderung einen Fehler erhalten, belassen sie den Port bei `8000`
:::

### Aufgabe 6.5: Intranet

Wenn ihr Computer und der ihrer Nachbaren im selben WLAN bzw. Netzwerk sind, sind die Voraussetzungen für ein Intranet gegeben.

Haben ihre Nachbaren die Website gestartet können sie anhand der IP-Adresse darauf zugreifen.

Zeigen sie ihre lokale IPv4-Adresse über die Netzwerkeinstellungen des Computers an. Dazu ein Beispiel wie das auf einem Linux-Computer aussieht:

![](../linux-ipv4.png)

Tauschen sie die IP-Adresse mit ihrem Nachbarn aus und rufen sie die Website im Browser damit auf. Beispiel: <http://192.168.1.104:8000>.
