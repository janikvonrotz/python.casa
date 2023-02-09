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