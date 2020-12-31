#!/usr/bin/env python3
from twython import Twython

# Information von der Registrierungswebseite
API_KEY =             'aWwD...'
API_SECRET =          '9qS9...'
ACCESS_TOKEN =        '1021...'
ACCESS_TOKEN_SECRET = 'qiwD...'
      
# Zugriff auf die API
tw = Twython(API_KEY, API_SECRET, ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 
                    
# Tweet senden
tw.update_status(status='Hello, Twitter!')

# Tweet senden
link = 'https://kofler.info/buecher/python'
with open('foto.jpg', 'rb') as f:
    response = tw.upload_media(media=f)
tw.update_status(
  status='Tweet mit Link und Bild: %s ' % (link),
  media_ids = [response['media_id']])
