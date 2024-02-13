from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["MONGO_URI"] = "mongodb+srv://USERNAME:PASSWORD@supplies.KEY.mongodb.net/DATABASE?retryWrites=true&w=majority"  
mongo = PyMongo(app)

app.template_folder = 'html'

from importRegister import open_register
from uploadPhoto import upload_photo
from resources import resources
from settings import settings
# from nonObjDiagnosis import diagnosis
from createSupply import create_supply
# from registering import register

# Load existing institutions from JSON file
try:
    with open('institutions.json', 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

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

    if users.get(institution) == password:
        return redirect(url_for('resources'))
    else:
        return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register():
    institution = request.form.get('institution')
    password = request.form.get('password')

    if institution not in users:
        users[institution] = password
        print(users)  # Print the users dictionary
        # Save updated institutions to JSON file
        with open('institutions.json', 'w') as f:
            json.dump(users, f)
        return redirect(url_for('login'))
    else:
        return "Institution already exists."

@app.route('/diagnosis')
def diagnosis():
    return render_template('diagnosis.html', hospitals=users.keys())

@app.route('/incoming_requests')
def incoming_requests():
    # Fetch diagnosis requests from the database or any source
    diagnosis_requests = [
        {"id": 1, "hospital": "Emory Hospital", "diagnosis": "Patient exhibits symptoms of viral infection; recommend rest and hydration"},
        {"id": 2, "hospital": "Grady Memorial", "diagnosis": "Preliminary diagnosis suggests allergic reaction; advise antihistamines and avoid allergens."},
        {"id": 3, "hospital": "Northside Hospital", "diagnosis": "Suspected fracture in the right arm; urgent X-ray and immobilization required."},
        {"id": 4, "hospital": "Methodist Hospital", "diagnosis": "Symptoms consistent with gastroenteritis; hydration and electrolyte balance crucial for recovery."}
        # Add more diagnosis requests as needed
    ]
    return render_template('incoming_requests.html', requests=diagnosis_requests)

if __name__ == '__main__':
    app.run(debug=True)
    
