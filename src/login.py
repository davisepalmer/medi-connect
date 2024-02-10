from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
from importRegister import open_register
from uploadPhoto import upload_photo
from resources import resources
from settings import settings
from nonObjDiagnosis import diagnosis
from createSupply import create_supply
from registering import register
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messaging

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['institution']
    password = request.form['password']
    
    # Dummy authentication
    if password == 'password':
        # Redirect to resources page
        return redirect(url_for('resources'))
    else:
        # If login fails, redirect back to login page with flash message
        app.logger.error('Login failed for username: %s', username)
        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('login'))

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)