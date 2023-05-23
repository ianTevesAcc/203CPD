from flask import Flask, request, render_template, redirect
import sqlite3
app = Flask(__name__)


@app.route('/user_info', methods=['GET'])
def main():  # put application's code here
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()

    received_data_obj = request.form
    data_obj_to_save = dict(received_data_obj)

    data_model = {
        'username': data_obj_to_save['username'],
        'email': data_obj_to_save['email'],
        'password': data_obj_to_save['password']

    }

    sql_query = """INSERT INTO users (username, email, password) VALUES (?,?,?)"""
    cursor.execute(sql_query, (data_model['username'], data_model['email'], data_model['password']))

    conn.commit()
    return redirect('/login')




@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')






    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #
    #     conn = sqlite3.connect('users.sqlite')
    #     c = conn.cursor()
    #
    #
    #     c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    #     user = c.fetchone()
    #
    #     if user:
    #         return redirect('/')
    #     else:
    #         error = 'Invalid username or password.'
    #         return render_template('login.html')
    #
    # return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)

