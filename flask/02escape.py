from flask import Flask

app = Flask(__name__)

from markupsafe import escape

@app.route("/h/<name>")
def hello(name):
    return f"<h1>Hello, {escape(name)}!</h1>"

@app.route("/s/<name>")
def selamat(name):
    return f"<h1>Selamat, {escape(name)}!</h1>"

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()