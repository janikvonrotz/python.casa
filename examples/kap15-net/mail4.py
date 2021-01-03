#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

html = '<html><body><p>Lorem ipsum<p>äöü ...</body></html>'
subj = 'Mail mit Foto äöü'
frm  = 'Sender mit äöü <bla@bla.com>'
to   = 'Empfänger mit äöü <bla@blabla.com>'

try:
    # E-Mail zusammenstellen
    mail = MIMEMultipart()
    mail['Subject'] = subj
    mail['From']    = frm
    mail['To']      = to
    mail.attach(MIMEText(html, 'html'))

    # Datei mit Foto hinzufügen
    with open('foto.jpg', 'rb') as f:
        img = MIMEImage(f.read())
    mail.attach(img)

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
    
