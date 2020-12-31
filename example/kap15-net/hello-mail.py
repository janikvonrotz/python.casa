#!/usr/bin/env python3
# dieses Beispiel funktioniert nur, wenn das Script
# auf einem Rechner ausgeführt wird, auf dem auch
# ein SMTP-Server läuft (also typischerweise auf
# einem Linux-Server)

from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg  = 'Lorem ipsum äöü ...'
subj = 'Die erste von Python versendete Mail äöü'
frm  = 'Absender <absender@host-abc.de>'
to   = 'Max Mustermann <max@mustermann.xyz>'

try:
    # E-Mail zusammenstellen
    mail = MIMEText(msg, 'plain', 'utf-8')
    mail['Subject'] = Header(subj, 'utf-8')
    mail['From']    = frm
    mail['To']      = to

    # E-Mail mit lokalem Mail-Server versenden
    smtp = smtplib.SMTP('localhost')
    smtp.send_message(mail)
    smtp.quit()
except BaseException as ex:
    print('Fehler:', ex)
