@app.route('/delete', methods=['POST'])
def delete():
    connection = sqlite3.connect("lager.db")
    cursor = connection.cursor()
    sql = "DELETE FROM lager WHERE id = %s" % (request.form['productID'])
    cursor.execute(sql)
    connection.commit()
    return redirect(url_for('list'))