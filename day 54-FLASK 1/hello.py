from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://t4.ftcdn.net/jpg/00/43/25/45/240_F_43254575_8UWOQGcx35mrQehQO9mEfmAvqLREhCJf.jpg" width=600>' \
           '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajlsN2M2d3FhNHR5NGJrbngwaHo1NXhiOHM1bXVsdTVkMjVpcXp5aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f5mF4TxqCkUog/giphy-downsized-large.gif">'


def make_bold(function):
    def wrapper_func():
        return f'<b>{function()}</b>'
    return wrapper_func
def make_emphasis(function):
    def wrapper_func():
        return f'<em>{function()}</em>'
    return wrapper_func
def make_underline(function):
    def wrapper_func():
        return f'<u>{function()}</u>'
    return wrapper_func

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_by():
    return "Bye"

# @app.route("/username/<name>")
# def  greet(name):
#     return f"Hello {name}!"

@app.route("/<name>")
def \
        greeet(name):
    return f"Hello {name}!"

# run automatically
if __name__ == "__main__":
    app.run(debug=True)


 # creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"