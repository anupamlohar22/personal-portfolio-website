import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        message = request.form['message']

        conn = sqlite3.connect('portfolio.db')

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO contacts(username,email,message) VALUES(?,?,?)",
            (username, email, message)
        )

        conn.commit()
        conn.close()

    return render_template('contact.html')

if __name__ == '__main__':
    app.run()