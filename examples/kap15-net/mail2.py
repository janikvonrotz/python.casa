#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg  = 'Lorem ipsum äöü ...'
subj = 'Noch eine von Python versendete Mail äöü'
frm  = 'Absender <absender@host-abc.de>'         
to   = 'Max Mustermann <max@mustermann.xyz>'

try:
    # E-Mail zusammenstellen
    mail = MIMEText(msg, 'plain', 'utf-8')
    mail['Subject'] = Header(subj, 'utf-8')
    mail['From']    = frm
    mail['To']      = to

    # E-Mail mit lokalem Mail-Server versenden
    # ersetzen Sie hostname, login und password
    # durch geeignete Zeichenketten!
    smtp = smtplib.SMTP('hostname')
    smtp.starttls()
    smtp.login('login', 'password')            
    smtp.sendmail(frm, [to], mail.as_string())
    smtp.quit()
except BaseException as ex:
    print('Fehler:', ex)
    
