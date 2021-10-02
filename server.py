from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_answer():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['userlocal'] = request.form['local']
    session['userlanguage'] = request.form['language']
    session['usercomments'] = request.form['comments']
    session['usermember'] = request.form['member']
    session['userupdates'] = request.form['updates']
    return redirect("/result")	 

@app.route('/result')
def show_user():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)