# Übungen Thema 12

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 12.1: Template anpassen

Auf dem Formular für *Produkt hinzufügen* steht auf dem Knopf `submit`. Benennen Sie die Text auf `Abschicken` um.

Sie wollen das die Kopfzeilen der Tabelle *Produkte* fett markiert werden. Fügen Sie den folgenden style-Tag am richtigen Ort im `layout.html` ein.

```html
<style>  
thead {
	font-weight: bold;
}
</style>
```

Sie möchten in der Navigation der Webapp neuen Link hinzu. Fügen die den a-Tag `<a href="https://python.casa">python.casa</a>` an der richtien Stelle im `layout.html` ein.

⭐ [Template anpassen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-12/Template%20anpassen)

### Aufgabe 12.2: Aktion Löschen hinzufügen

Sie möchten eine neue Funktion in der Webapplikation einbauen. Benutzer sollen Produkte löschen können. Dazu haben diese Code-Teile erstellt:

**app.py**

```python
@app.route('/delete', methods=['POST'])
def delete():
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = "DELETE FROM lager WHERE id = %s" % (request.form['productID'])
    cursor.execute(sql)
    connection.commit()
    return redirect(url_for('list'))
```

**list.index**

```html
{% extends "layout.html" %}
{% block content %}
<h1>Produktliste</h1>
<table>
  <thead>
    <td>ID</td>
    <td>Name</td>
    <td>Referenz</td>
    <td>Barcode</td>
    <td>Lager</td>
    <td>Preis</td>
    <td>Aktion</td>
  </thead>
  {% for row in data %}
  <tr>
    <td>{{row[0]}}</td>
    <td>{{row[1]}}</td>
    <td>{{row[2]}}</td>
    <td>{{row[3]}}</td>
    <td>{{row[4]}}</td>
    <td>{{row[5]}}</td>
    <td>
      <form action="{{ url_for('delete') }}" method="post">
        <input type="hidden" name="productID" value="{{row[0]}}">
        <input type="submit" value="Löschen" />
      </form>
    </td>
  </tr>
  {% endfor %}
</table>
{% endblock %}
```

Aktualisieren Sie die entsprechenden Dateien und starten Sie Webapplikation.

⭐ [Aktion Löschen hinzufügen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-12/Aktion%20Löschen%20hinzufügen)

### Aufgabe 12.3: Xlsx-Export hinzufügen

Wir möchten die Daten aus der Datenbank in eine Excel-Datei exportieren. Dazu erstellen Sie eine Funktion, die den Export ausführt und passen die Weboberfläche an.

Fügen Sie die folgende Datei dem Projekt hinzu und ergänzen Sie alle mit `# Kommentar` markierten Zeile mit einem Kommentar. Versuchen Sie den Code zu verstehen.

**export.py**

```python
# Kommentar
from xlsxwriter.workbook import Workbook
import sqlite3

def xlsx():
    # Kommentar
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    
    # Kommentar
    sql = "SELECT * FROM lager"
    cursor.execute(sql)
    data = cursor.fetchall()

    # Kommentar
    workbook = Workbook('output.xlsx')
    # NKommentar
    worksheet = workbook.add_worksheet()
    # Kommentar
    worksheet.write(0, 0, "ID")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "Referenz")
    worksheet.write(0, 3, "Barcode")
    worksheet.write(0, 4, "Lager")
    worksheet.write(0, 5, "Preis")

    # Kommentar
    for index, record in enumerate(data):
        # Kommentar
        index = index+1
        # Kommentar
        worksheet.write(index, 0, record[0])
        worksheet.write(index, 1, record[1])
        worksheet.write(index, 2, record[2])
        worksheet.write(index, 3, record[3])
        worksheet.write(index, 4, record[4])
        worksheet.write(index, 5, record[5])

    # Kommentar
    connection.close()
    workbook.close()
```

Wie Sie gesehen haben, braucht es die zum Ausführen der Funktion das Paketr [XlsxWriter](https://pypi.org/project/XlsxWriter/). Installieren Sie es mit dem Pip Manager oder führen Sie den Befehl `pip install XlsxWriter` im Terminal aus.

In der `app.py` fügen Sie zuoberst den Import-Befehl hinzu.

```python
import export
```

Und vor dem Aufruf der `__main__` Funktion erstellen Sie die Route für den Export.

```python
@app.route('/file')
def file():
    export.xlsx()
    return send_file('output.xlsx', attachment_filename='output.xlsx')
```

Als letztes ersetzen Sie den Inhalt des `index.html` Template mit diesem Inhalt:

```html
{% extends "layout.html" %}
{% block content %}
<h1>Aktionen</h1>
<p><a href="/insert">Produkt hinzufügen</a></p>
<p><a href="/list">Produkte auflisten</a></p>
<p><a href="/file">output.xlsx herunterladen</a></p>
{% endblock %}
```

⭐ [Xlsx-Export hinzufügen](https://github.com/janikvonrotz/python.casa/blob/main/topic-12/Xlsx-Export%20hinzufügen)

### Aufgabe 12.4: Aktion Bearbeiten hinzufügen

**app.py**

```python
@app.route('/edit/<id>')
def edit(id):
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = f"SELECT * FROM lager WHERE id = {id}"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("edit.html", data=data[0])

@app.route('/save', methods=['POST'])
def save():
    message=""
    if request.method == 'POST':
        connection = sqlite3.connect("lager.db")
        cursor = connection.cursor()
        sql = f"""
        UPDATE lager SET
        name = '{request.form['name']}',
        referenz = '{request.form['referenz']}',
        barcode = '{request.form['barcode']}',
        lager = '{request.form['lager']}',
        preis = '{request.form['preis']}'
        WHERE id = '{request.form['id']}'
        """
        print(sql)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return redirect(url_for('list'))
```

**template/list.hmtl**

```html
{% extends "layout.html" %}
{% block content %}
<h1>Produktliste</h1>
<table>
  <thead>
    <td>ID</td>
    <td>Name</td>
    <td>Referenz</td>
    <td>Barcode</td>
    <td>Lager</td>
    <td>Preis</td>
    <td>Aktion</td>
  </thead>
  {% for row in data %}
  <tr>
    <td>{{row[0]}}</td>
    <td><a href="/edit/{{row[0]}}">{{row[2]}}</a></td>
    <td>{{row[2]}}</td>
    <td>{{row[3]}}</td>
    <td>{{row[4]}}</td>
    <td>{{row[5]}}</td>
    <td>
      <form action="{{ url_for('delete') }}" method="post">
        <input type="hidden" name="productID" value="{{row[0]}}">
        <input type="submit" value="Löschen" />
      </form>
    </td>
  </tr>
  {% endfor %}
</table>
{% endblock %}
```

**template/edit.html**

```html
{% extends "layout.html" %}
{% block content %}
<h1>Produkt bearbeiten</h1>
<form action="{{ url_for('save') }}" method="POST">
    <fieldset>
        <input type="hidden" name="id" value="{{data[0]}}">
        <label for="name">Name:</label>
        <input required type="text" name="name" value="{{data[1]}}"/><br><br>
        <label for="referenz">Referenz:</label>
        <input required type="text" name="referenz" value="{{data[2]}}"/><br><br>
        <label for="barcode">Barcode:</label>
        <input required type="text" name="barcode" value="{{data[3]}}"/><br><br>
        <label for="lager">Lager:</label>
        <input required type="number" name="lager" value="{{data[4]}}"/><br><br>
        <label for="preis">Preis:</label>
        <input required type="number" name="preis" value="{{data[5]}}"/>
    </fieldset>
    <input type="submit" value="Speichern" />
</form>
{% endblock %}
```

⭐ [Aktion Bearbeiten hinzufügen](https://github.com/janikvonrotz/python.casa/blob/main/topic-12/Xlsx-Export%20hinzufügen)