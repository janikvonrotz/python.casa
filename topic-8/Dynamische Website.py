from datetime import datetime 

html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>HTML mit Erstelldatum</title>
</head>
<body>
  <p>Erstellt am {datetime.today()}.</p>
</body>
</html>
"""

with open('website.html', 'w') as file:
	file.write(html)