from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Tell Flask to look for templates in the 'pages' folder
app.template_folder = 'html'

# Dummy user data (replace with your actual user data or database)
users = {
    'admin': 'password'
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
    return render_template('resources.html')

@app.route('/diagnosis')
def diagnosis():
    return render_template('diagnosis.html')

@app.route('/create_supply', methods=['POST'])
def create_supply():
    data = request.get_json()
    supply_name = data.get('supplyName')
    quantity = data.get('quantity')
    requested_by = data.get('requestedBy')
    new_supply = Supply(True,supply_name, quantity, requested_by) #isneeded functionality needs to be added
    return jsonify({'message': 'Supply created successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
