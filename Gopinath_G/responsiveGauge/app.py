from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    percent =  0.7
    return render_template("index.html", receive=percent)