from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('username')
    password = request.form.get('password')
    return f"<h1>Thank you, {name}, for submitting your password: {password}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)