from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    message=""
    if request.method == 'POST':
        name = request.form['name']
        referenz = request.form['referenz']
        barcode = request.form['barcode']
        lager = request.form['lager']
        preis = request.form['preis']
        connection = sqlite3.connect("lager.db")
        cursor = connection.cursor()
        sql = "INSERT INTO lager(name,referenz,barcode,lager,preis) VALUES('%s', '%s', '%s', %s, %s)" % (name,referenz,barcode,lager,preis)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        message="Produkt hinzugefügt."
    return render_template("submit.html", message=message)

@app.route('/list')
def list():
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM lager"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("list.html", data=data)

if __name__ == '__main__':
   app.run(debug = True)