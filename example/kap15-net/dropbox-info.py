#!/usr/bin/env python3
import dropbox

# Damit Sie dieses Beispiel testen können, brauchen Sie einen Dropbox-Account.
# Außerdem müssen Sie unter https://www.dropbox.com/developers/apps eine neue
# Dropbox-App einrichten und danach ein 'access token' generieren. Die
# resultierende Zeichenkette geben Sie unten ein.

db = dropbox.Dropbox('xxx-access-token')
print(db.users_get_current_account())
