from flask import Flask, render_template
from quotes import generate_quote

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Ann"):
    context = {
        "quote": generate_quote(name),
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run()
