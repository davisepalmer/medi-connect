# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_pymongo import PyMongo

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Required for flash messaging

# # Setup PyMongo
# app.config["MONGO_URI"] = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"
# mongo = PyMongo(app)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         institution = request.form.get('institution')
#         password = request.form.get('password')

#         # Check if the institution already exists
#         if mongo.db.users.find_one({"institution": institution}):
#             flash('Institution already exists. Please choose a different name.', 'error')
#         else:
#             # Insert the new institution into the database
#             mongo.db.users.insert_one({
#                 "institution": institution,
#                 "password": password
#             })
#             flash('Institution registered successfully!', 'success')
#             return redirect(url_for('login'))

#     return render_template('register.html')
