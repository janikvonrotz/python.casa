#!/usr/bin/env python3
import pymysql.cursors
from datetime import date, datetime, timedelta

today = datetime.now().date()  
day = timedelta(days=1)
past = str(today - 90 * day)
sql = """SELECT COUNT(*) AS cnt, 
                COUNT(DISTINCT id_person) AS cnt_distinct 
         FROM login 
         WHERE ts>'""" + past + "'"

# Liste aller Datenbanken einlesen
with open('dbs.txt') as f:
    dbs = f.readlines()
dbs = [ db.strip() for db in dbs ]  # /n entfernen

try:
    # Verbindungsaufbau
    conn = pymysql.connect(host='localhost',
                           user='adminuser',
                           password='strenggeheim',
                           db=dbs[0],
                           charset='utf8mb4',
                           cursorclass=\
                             pymysql.cursors.DictCursor)
                            
    
    # alle Datenbanken durchlaufen
    results = []
    for db in dbs:
        conn.select_db(db)
        
        with conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchone()
            results += [{'name': db, 'result': result}]


except BaseException as ex:
    print('Fehler:', ex)
finally:
    conn.close()

# Auswertung
results.sort(reverse=True,
             key=lambda itm: itm['result']['cnt'])
for itm in results:
    print('%25s %5d %5d' % 
          (itm['name'], itm['result']['cnt'], 
           itm['result']['cnt_distinct']))
