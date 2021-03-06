from flask import Flask, request, render_template, redirect, url_for, session




app = Flask(__name__)



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)