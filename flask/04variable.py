from flask import Flask

app = Flask(__name__)

from markupsafe import escape

@app.route('/user/<username>')
@app.route('/user/<username>/<nama>')
def show_user_profile(username,nama=None):
    # show the user profile for that user
    return f'User {escape(username)} dan nama {escape(nama)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()