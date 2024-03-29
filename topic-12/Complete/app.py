from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
app = Flask(__name__)
import export

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

@app.route('/delete', methods=['POST'])
def delete():
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = "DELETE FROM lager WHERE id = %s" % (request.form['productID'])
    cursor.execute(sql)
    connection.commit()
    return redirect(url_for('list'))

@app.route('/file')
def file():
    export.xlsx()
    return send_file('output.xlsx')

@app.route('/edit/<id>')
def edit(id):
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = f"SELECT * FROM lager WHERE id = {id}"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("edit.html", data=data[0])

@app.route('/save', methods=['POST'])
def save():
    message=""
    if request.method == 'POST':
        connection = sqlite3.connect("lager.db")
        cursor = connection.cursor()
        sql = f"""
        UPDATE lager SET
        name = '{request.form['name']}',
        referenz = '{request.form['referenz']}',
        barcode = '{request.form['barcode']}',
        lager = '{request.form['lager']}',
        preis = '{request.form['preis']}'
        WHERE id = '{request.form['id']}'
        """
        print(sql)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return redirect(url_for('list'))

if __name__ == '__main__':
   app.run(debug = True)