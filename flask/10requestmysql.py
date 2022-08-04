from flask import Flask
from flask import render_template

app = Flask(__name__)

from flask import request

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="mpi",password="mpi",database="mpitest")
mycursor = mydb.cursor()

@app.route('/input', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            sql = "INSERT INTO tabelnum (suhu,kelembaban) VALUES (%s, %s)"
            mycursor.execute(sql,(request.form['suhu'],request.form['kelembaban']))
            mydb.commit()
            return render_template('formmysql.html',pesan="Input Skses")
        except:
            return render_template('formmysql.html',pesan="Input Gagal")
    else:
        return render_template('formmysql.html')

@app.route("/")
def index():
    mycursor.execute("SELECT * FROM tabelnum")
    myresult = mycursor.fetchall()
    return render_template('loopmysql.html',data=myresult)