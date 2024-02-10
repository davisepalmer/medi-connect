from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
@app.route('/resources')
def resources():
    supplies = mongo.db.supplies.find()
    giving = mongo.db.giving.find()
    return render_template('resources.html', supplies=supplies, giving=giving)
    