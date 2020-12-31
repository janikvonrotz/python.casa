#!/usr/bin/env python3
import dropbox

# Damit Sie dieses Beispiel testen können, brauchen Sie einen Dropbox-Account.
# Außerdem müssen Sie unter https://www.dropbox.com/developers/apps eine neue
# Dropbox-App einrichten und danach ein 'access token' generieren. Die
# resultierende Zeichenkette geben Sie unten ein.



try:
    db = dropbox.Dropbox('xxx-access-token')
    # alle Dateien ermitteln
    for entry in db.files_list_folder('').entries:
        print(entry.name)
    localfname =  'image-from-dropbox.jpg'
    dropboxname = '/upload.jpg'
    db.files_download_to_file(localfname, dropboxname)

except BaseException as ex:
    print('Fehler', ex)


