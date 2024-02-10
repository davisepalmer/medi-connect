from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app import app, mongo
@app.route('/diagnosis/upload', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    photo = request.files['photo']

    # Perform diagnosis process with the uploaded photo here
    # You can save the photo to a directory, process it, and return the diagnosis result
    
    # Example: Saving the photo to a directory
    photo.save('uploads/' + photo.filename)

    return jsonify({'message': 'Photo uploaded successfully'}), 200
