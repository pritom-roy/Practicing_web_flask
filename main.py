from flask import Flask
import random

app = Flask(__name__)


# def make_bold(function):
#     def wrapper():
#         value = function()
#         return f"<b>{value}<b>"
#
#     return wrapper


@app.route("/<int:name>")
def hello_world(name):
    guess = random.randint(0, 9)
    print(guess)

    if name == guess:
        return '<h1>Guess a number between 0 and 9<h1>' \
               '<img src="https://img.freepik.com/free-vector/branch-sakura-flowers-hand-drawn-cartoon-art' \
               '-illustration_56104-582.jpg?w=2000" width=400> '

    else:
        return '<h1>Guess a number between 0 and 9<h1>' \
               '<h1>Wrong answer<h1>'


if __name__ == "__main__":
    app.run(debug=True)
