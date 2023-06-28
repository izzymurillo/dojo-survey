from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)