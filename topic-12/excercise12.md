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

### Aufgabe 12.3: Excel-Export hinzügen

⭐ [Excel-Export hinzufügen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-12/Exccel-Export%20hinzufügen)

### Aufgabe 12.4: Aktion Bearbeiten hinzufügen

