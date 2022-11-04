from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Sherlock@221B"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", Great to see you!")
    return render_template("index.html")