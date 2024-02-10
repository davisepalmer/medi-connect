from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["MONGO_URI"] = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"  
mongo = PyMongo(app)

app.template_folder = 'html'

from importRegister import open_register
from uploadPhoto import upload_photo
from resources import resources
from settings import settings
from nonObjDiagnosis import diagnosis
from createSupply import create_supply
from registering import register


users = {
    'Hospital 1': 'password',
    'Hospital 2': 'password',
    'Hospital 3': 'password',
    'Hospital 4': 'password',
    'Hospital 5': 'password'
}

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/login')
def login():
    return render_template('login.html', users=users)

@app.route('/login', methods=['POST'])
def login_post():
    institution = request.form.get('institution')
    password = request.form.get('password')

    # Check if institution and password match the dummy user data
    #if users.get(institution) == password:
    if password == "password":
        # Successful login, redirect to resources page
        return redirect(url_for('resources'))
    else:
        # Failed login, redirect back to login page
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)