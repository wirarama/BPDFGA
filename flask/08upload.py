from flask import Flask
from flask import render_template

app = Flask(__name__)

from flask import request
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        try:
            f = request.files['namafile']
            f.save(f"/Users/wirarama/python/FGA/BPDFGA/flask/upload/{secure_filename(f.filename)}")
            return render_template('formfile.html',pesan="Upload Sukses")
        except:
            return render_template('formfile.html',pesan="Upload Gagal")
    else:
        return render_template('formfile.html')
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()