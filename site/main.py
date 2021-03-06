from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os
from datastax_functions import createUser, getUserID, getUserData, checkUser, userExists, createFund, addToFund

load_dotenv()



app = Flask(__name__)
app.secret_key=os.environ.get("FLASK_SESSION_KEY")


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('landing.html')

#signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        
        if userExists(username):
            return redirect(url_for('signup'))
        else:
            createUser(username, password)
            session['username'] = username
            return redirect(url_for('newFund'))
    elif request.method=='GET':
        return render_template('signup.html')


    elif request.method=='GET':
        return render_template('login.html')

#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        if checkUser(username, password):
            session['username'] = username
            return redirect(url_for('newFund'))
        else:
           return redirect(url_for('login'))


    elif request.method=='GET':
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('home'))

@app.route('/newFund', methods=['GET', 'POST'])
def newFund():
    if request.method=='GET':
        return render_template('dashboard.html')

    elif request.method=='POST':
        fundName = request.form['fundName']
        fundDesc = request.form['fundDesc']
        fundGoal = request.form['fundGoal']
        fundCreator = session['user']
        createFund(fundName, fundDesc, fundGoal)
        return redirect(url_for('fund'))

@app.route('/fund')
def fund():
    fundData = getUserData(session['username'])
    return render_template('fund.html', fundData)

@app.route('/addFunds', methods = ['POST'])
def addFunds():
    amount = request.form['amount']
    #creator = ??
    fundName = request.form['fundName']

    return redirect(url_for('fund'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)