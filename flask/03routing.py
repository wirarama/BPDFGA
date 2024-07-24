from flask import Flask

app = Flask(__name__)
nav = '<a href="">Home</a> | <a href="/hello">Hello</a> | <a href="/produk">Produk</a>'
@app.route('/')
def index():
    return nav+'Index Page'

@app.route('/hello')
def hello():
    return nav+'Hello, World'

@app.route('/produk')
def produk():
	out = "<ul>"
	for x in range(100):
		out += "<li>produk no "+str(x)+"</li>"
	out += "</ul>"
	return nav+out

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()