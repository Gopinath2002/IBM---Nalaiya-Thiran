from flask import Flask,render_template,url_for,request

app= Flask(__name__)
    
@app.route('/', methods = ["GET","POST"])
def predict():
    return render_template("index.html")     


@app.route('/result', methods = ["GET","POST"])
def result():
    if request.method == 'POST':
        percentage = int(request.form['CutOff'])
    return render_template("index.html" ,percent=percentage)     



if __name__=='__main__':
    app.run(debug=True)