import export

@app.route('/file')
def file():
    export.xlsx()
    return send_file('output.xlsx', attachment_filename='output.xlsx')
