from flask import Flask
from flask import render_template,redirect,request

app = Flask(__name__)

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="mpitest")
mycursor = mydb.cursor()

@app.route('/edit/<edit>', methods=['GET', 'POST'])
def editku():
    if request.method == 'POST':
        try:
            sql = "UPDATE tabelnum SET suhu='%s',kelembaban='%s' WHERE id='%s'"
            mycursor.execute(sql,(request.form['suhu'],request.form['kelembaban'],{escape(edit)}))
            mydb.commit()
            return redirect('http://127.0.0.1:5000/')
            #return render_template('formmysql.html',pesan="Input Skses")
        except:
            return redirect('http://127.0.0.1:5000/')
            #return render_template('formmysql.html',pesan="Input Gagal")
    else:
        sql = f"SELECT suhu,kelembaban FROM tabelnum WHERE id='{escape(edit)}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return render_template('formmysql.html',edit=myresult)

@app.route('/input', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            sql = "INSERT INTO tabelnum (suhu,kelembaban) VALUES (%s, %s)"
            mycursor.execute(sql,(request.form['suhu'],request.form['kelembaban']))
            mydb.commit()
            return redirect('http://127.0.0.1:5000/')
            #return render_template('formmysql.html',pesan="Input Skses")
        except:
            return redirect('http://127.0.0.1:5000/')
            #return render_template('formmysql.html',pesan="Input Gagal")
    else:
        return render_template('formmysql.html')

@app.route("/")
def index():
    mycursor.execute("SELECT * FROM tabelnum")
    myresult = mycursor.fetchall()
    return render_template('loopmysql.html',data=myresult)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()