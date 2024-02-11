from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
from pymongo import MongoClient

@app.route('/decrement')
def decrement():
    mongo_uri = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"  
    client = MongoClient(mongo_uri)
    db = client.get_default_database()
    collection = db["database"]
    decrement = {}