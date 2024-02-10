from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messaging

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['institution']
    password = request.form['password']
    
    # Dummy authentication
    if password == 'password':
        # Redirect to resources page
        return redirect(url_for('resources'))
    else:
        # If login fails, redirect back to login page with flash message
        app.logger.error('Login failed for username: %s', username)
        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('login'))

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register')
def register():
    return render_template('register.html')