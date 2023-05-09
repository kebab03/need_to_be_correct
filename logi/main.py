from flask import Flask, request, render_template, jsonify, session,redirect
app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Simple in-memory user database
users = {
    'admin': 'adminpass',
    'user': 'userpass'
}

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/toggle')
        else:
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

# Define the logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

# Define the toggle switch page route
@app.route('/toggle')
def toggle():
    if 'username' not in session:
        return redirect('/login')
    return render_template('toggle.html', state=state)

# Define the /state route
@app.route('/state')
def get_state():
    if 'username' not in session:
        return jsonify(error='Unauthorized access')
    return jsonify(switch=state)

# Define the toggle switch state route
@app.route('/toggle-state', methods=['POST'])
def toggle_state():
    if 'username' not in session:
        return jsonify(error='Unauthorized access')
    global state
    state = 'on' if state == 'off' else 'off'
    return jsonify(switch=state)

if __name__ == '__main__':
    state = 'on'
    app.run(debug=True)

