from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os
from datastax_functions import createUser, getUserID, getUserData, checkUser, userExists, 

#load_dotenv()



app = Flask(__name__)
#app.secret_key=os.environ.get("SECRET_KEY")


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World!"
    #return render_template('landing.html')

#signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        
        if userExists(username):
            return redirect(url_for('signup'))
        else:
            createUser(username, password)
            session['username'] = username
            return redirect(url_for('map'))
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
            return redirect(url_for('map'))
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
        return render_template('newFund.html')

    elif request.method=='POST':
        fundName = request.form['fundName']
        fundDesc = request.form['fundDesc']
        fundGoal = request.form['fundGoal']
        #fundCreator = session['user']

        return redirect(url_for('fund'))

@app.route('/fund')
def fund():
    return render_template('fund.html', fund)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)