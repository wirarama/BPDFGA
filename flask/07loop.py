from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = [
    ["jeruk",20000],
    ["apel",67000],
    ["salak",12000],
    ["semangka",40000],
    ["nanas",56000]
    ]
    return render_template('loop.html',data=data)
