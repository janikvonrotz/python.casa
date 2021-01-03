#!/usr/bin/env python3
import dropbox

# Damit Sie dieses Beispiel testen können, brauchen Sie einen Dropbox-Account.
# Außerdem müssen Sie unter https://www.dropbox.com/developers/apps eine neue
# Dropbox-App einrichten und danach ein 'access token' generieren. Die
# resultierende Zeichenkette geben Sie unten ein.

db = dropbox.Dropbox('xxx-access-token')
fname = 'foto.jpg'     # Name einer lokalen Datei
dname = '/upload.jpg'  # Name der Datei in Dropbox
try:
    with open(fname, 'rb') as f:
        response = db.files_upload(f.read(), dname)
    print('uploaded:', response)
except BaseException as ex:
    print('Fehler', ex)


