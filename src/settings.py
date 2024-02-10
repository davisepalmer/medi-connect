from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo

@app.route('/settings')
def settings():
    return render_template('settings.html')

