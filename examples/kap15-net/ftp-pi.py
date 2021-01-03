#!/usr/bin/env python3
from ftplib import FTP

host = 'raspberry'
user = 'pi'
pw   = 'geheim'

try:
    # Datei readme.txt vom FTP-Server herunterladen
    # und lokal speichern
    ftp = FTP(host, user, pw)
    fname = 'readme.txt'
    with open(fname, 'wb') as file:
        ftp.retrbinary('RETR %s' % (fname), file.write)
        
    # lokale Datei auf den FTP-Server hochladen
    fname = 'other.txt'
    with open(fname, 'rb') as file:
        ftp.storbinary('STOR %s' % (fname), file)
except BaseException as ex:
    print('Fehler:', ex)
    




