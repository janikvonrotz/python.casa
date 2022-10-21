## Archiv

---
### Heap anzeigen

Mit Thonny können wir sehen wie Python die Variablen und deren Werte verwaltet.

🎬 In Tonny Menu *Ansicht* anwählen und die Optionen *Heap* und *Variablen* aktivieren.

---
### Variablen anzeigen

> Variablen sind lediglich Referenzen

🎬 Folgende Aktionen in Thonny ausführen:
* Neues leeres Skript erstellen
* Datei speichern im neuen Ordner `Thema2` als `Heap.py`
* Anweisung `x=1` eingeben und ausführen

---
### Ergebnis Heap

Eine Variable ist eine Referenz zu einem Eintrag im Heap.

![](../thonny-variables-and-heap.png)

---
### Kommutativ

🎬 In der Python-Shell ausführen:

```python
(a and b) == (b and a)
(a or b) == (b or a)
```

---
### Assoziativ

🎬 In der Python-Shell ausführen:

```python
c = True
((a and b) and c) == (a and (b and c))
((a or b) or c) == (a or (b or c))
```

---
### Distributiv

🎬 In der Python-Shell ausführen:

```python
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)
```

---
### Komplentär / Idempotenz

🎬 In der Python-Shell ausführen:

```python
(a or not a) == 1
(a and not a) == 0
```

---
### de Morgan

🎬 In der Python-Shell ausführen:

```python
not (a or b) == (not a and not b)
not (a and b) == (not a or not b)
```

---
### Neutralität / Extremal

🎬 In der Python-Shell ausführen:

```python
(a or 0) == a
(a and 1) == a
```