from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["MONGO_URI"] = "mongodb+srv://new-user-2:qy5T1AM3I9oCN8tk@supplies.nyyixjh.mongodb.net/<database>?retryWrites=true&w=majority"  # username: new-user-2, password: password1
mongo = PyMongo(app)


# Tell Flask to look for templates in the 'pages' folder
app.template_folder = 'html'

# Dummy user data (replace with your actual user data or database)
users = {
    'admin': 'password',
    'hospitalA': 'password',
    'hospitalB': 'password'
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if username and password match the dummy user data
    if users.get(username) == password:
        # Successful login, redirect to resources page
        return redirect(url_for('resources'))
    else:
        # Failed login, redirect back to login page
        return redirect(url_for('login'))

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/resources')
def resources():
    supplies = mongo.db.supplies.find()
    return render_template('resources.html', supplies=supplies)

@app.route('/diagnosis')
def diagnosis():
    return render_template('diagnosis.html')

@app.route('/create_supply', methods=['POST'])
def create_supply():
    data = request.get_json()
    supply_name = data.get('supplyName')
    quantity = data.get('quantity')
    requested_by = data.get('requestedBy')

    if supply_name and quantity and requested_by:
        mongo.db.supplies.insert_one({
            "isNeeded": True,
            "item": supply_name,
            "quantity": quantity,
            "originHosp": requested_by
        })
        return jsonify({'message': 'Supply created successfully'}), 200
    else:
        return jsonify({'error': 'Invalid supply data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
