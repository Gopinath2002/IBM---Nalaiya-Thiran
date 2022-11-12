from flask import Flask, render_template, request, flash

app = Flask(__name__)


app.secret_key="gopinath25"

@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['Name']) + ", great to see you")
    return render_template("index.html")