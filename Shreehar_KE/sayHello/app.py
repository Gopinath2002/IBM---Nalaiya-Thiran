from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Sherlock@221B"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")