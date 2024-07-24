from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Selamat pagi</h1><h2>sub judul</h2>"

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()