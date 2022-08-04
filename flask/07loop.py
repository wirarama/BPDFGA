from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = ["jeruk","apel","salak","semangka","nanas"]
    return render_template('loop.html',data=data)
