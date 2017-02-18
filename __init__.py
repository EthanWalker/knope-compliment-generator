from flask import Flask, render_template, send_from_directory
import os
from quotes import generate_quote


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/')
@app.route('/<name>')
def index(name="Ann"):
    return render_template("index.html",
                           quote=generate_quote(name))

if __name__ == "__main__":
    app.run()
