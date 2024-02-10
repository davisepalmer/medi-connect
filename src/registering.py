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
