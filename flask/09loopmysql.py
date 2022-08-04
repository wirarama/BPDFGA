from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="mpi",
      password="mpi",
      database="mpitest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tabelnum")
    myresult = mycursor.fetchall()
    return render_template('loopmysql.html',data=myresult)
