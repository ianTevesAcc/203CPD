from flask import Flask, request, render_template, redirect
import sqlite3
app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Check if the username already exists
        c.execute('SELECT * FROM users WHERE username=? OR email=?', (username, email))
        existing_user = c.fetchone()


        if existing_user:
            error = 'Username already exists.'
            return render_template('register.html')

        # Insert the new user into the database
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Retrieve the user from the database
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()

        if user:
            return redirect('/')
        else:
            error = 'Invalid username or password.'
            return render_template('login.html')

    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)

