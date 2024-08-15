from flask import Flask
import random

app = Flask(__name__)
RANDOM_NUMBER = random.randint(0, 9)


@app.route("/")
def guess_main():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmxkbWNlcWVlN3RlZnl3aDV1bXptNjFmbXVicHRjOXo4dW02aDhkZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p9rzjg5Kle8nFbfa6o/giphy-downsized-large.gif' width=800>" \

@app.route("/<int:number>")
def guess_number(number):
    if RANDOM_NUMBER > number:
        return "<h1 style='color: red'>Your guess was too low, guess again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZnbDQybnBxeTBycTl4cWJsdHI0NG0zMG1udXh2MjU4dnJkNGw2cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/znMZaxLa4IGWMl2ZME/giphy-downsized-large.gif'/>"
    if RANDOM_NUMBER < number:
        return "<h1 style=\"color: green\">You guessed correct</h1>" \
                   "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmh2eHhkeHpvcHdpaXRrczBldm1rMmFmc3AxaGZoMGFsNjZxYzEyaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ksvNgvFPsip6iR4cgW/giphy.gif'/>"
    else:
        return "<h1 style='color: purple'>You guessed too high, try again</h1>"\
            "img src='https://giphy.com/embed/3rh4e38JfzpXXBWc1z/video'/>"


if __name__ == "__main__":
    app.run(debug=True)
