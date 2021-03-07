from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os
from datastax_functions import createUser, getUserID, getUserData, checkUser, userExists, createFund, addToFund, getFundsList, getFund

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
            return redirect(url_for('dashboard'))
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
            return redirect(url_for('dashboard'))
        else:
           return redirect(url_for('login'))


    elif request.method=='GET':
        return render_template('landing.html')
    
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    data = getUserData(getUserID(session['username']))
    print(data)
    return render_template('dashboard.html', data=data)


@app.route('/newFund', methods=['GET', 'POST'])
def newFund():
    if request.method=='GET':
        return render_template('createfund.html')

    elif request.method=='POST':
        fundName = request.form['name-fund']
        fundDesc = request.form['description']
        fundGoal = request.form['goal']
        fundCreator = session['username']
        createFund(fundName, fundDesc, fundGoal, fundCreator)
        return redirect(url_for('fund', username=fundCreator, fundName=fundName))

@app.route('/fund/<username>/<fundName>')
def fund(username, fundName):
    fundData = getFund(username, fundName)
    return render_template('view.html', data = fundData, creator=username)

@app.route('/addFunds', methods = ['POST'])
def addFunds():
    select = request.form.get('selectedFund')
    print(select)

    amount = request.form['amount']
    print(amount)

    fundData = select.split(',')
    fundName = fundData[0]
    creator = fundData[1]
    print(fundName)
    print(creator)
    addToFund(fundName, creator, amount)
    return redirect("http://0.0.0.0:5000/fund/" + creator +"/"+ fundName)

@app.route('/getFundList', methods = ['GET'])
def getFundList():
    return getFundsList()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)