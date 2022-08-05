from flask import Flask
from flask import render_template

app = Flask(__name__)

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pesan = request.form['email']+"<br>"+request.form['password']+"<br>"+request.form['cek']
        return render_template('form.html',pesan=pesan)
    else:
        return render_template('form.html')
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()