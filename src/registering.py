from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
users = {
    'Hospital 1': 'password',
    'Hospital 2': 'password',
    'Hospital 3': 'password',
    'Hospital 4': 'password',
    'Hospital 5': 'password'
}
@app.route('/register')
def register():
    # if request.method == 'POST':
    institution = request.form.get('institution')
    password = request.form.get('password')
    users[institution] = password

    # # Check if the institution already exists
    # if institution in users:
    #     flash('Institution already exists. Please choose a different name.', 'error')
    # else:
    #     # Add the new institution to the institutions dictionary
    #     users[institution] = password
    #     flash('Institution registered successfully!', 'success')

    # return render_template('login.html')
    return redirect(url_for('login'))