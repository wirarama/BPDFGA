from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/produk')
def produk():
	out = "<ul>"
	for x in range(100):
		out += "<li>produk no "+str(x)+"</li>"
	out += "</ul>"
	return out