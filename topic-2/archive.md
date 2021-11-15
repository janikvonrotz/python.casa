## Archiv

---
### Kommutativ

🎬 In der Python-Shell ausführen:

```py
(a and b) == (b and a)
(a or b) == (b or a)
```

---
### Assoziativ

🎬 In der Python-Shell ausführen:

```py
c = True
((a and b) and c) == (a and (b and c))
((a or b) or c) == (a or (b or c))
```

---
### Absorption

🎬 In der Python-Shell ausführen:

```py
(a or (a and b)) == a
(a and (a or b)) == a
```

---
### Distributiv

🎬 In der Python-Shell ausführen:

```py
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)
```

---
### Komplentär / Idempotenz

🎬 In der Python-Shell ausführen:

```py
(a or not a) == 1
(a and not a) == 0
```

---
### de Morgan

🎬 In der Python-Shell ausführen:

```py
not (a or b) == (not a and not b)
not (a and b) == (not a or not b)
```

---
### Neutralität / Extremal

🎬 In der Python-Shell ausführen:

```py
(a or 0) == a
(a and 1) == a
```