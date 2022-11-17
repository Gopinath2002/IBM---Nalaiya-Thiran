from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def welcome():

    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):

    res=""

    if score>=50:
        res="PASS"

    else:
        res="FAIL"

    return render_template('result.html',result=res)


@app.route('/results/<int:marks>')
def results(marks):

    result=""

    if marks<50:
        result='fail'

    else:
        result='success'

    return redirect(url_for(result,score=marks))


@app.route('/submit/',methods=['POST','GET'])
def submit():

    total_score=0

    if request.method=='POST':
        english=float(request.form['english'])
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        total_score=(english+maths+science)/3

    res=""

    return redirect(url_for('success',score=total_score))

    
if __name__=='__main__':
    app.run(debug=True)