from flask import Flask
from random import randint


# Create instance of Flask
app = Flask(__name__)

# Set the correct number, and print to console for testing purposes
correct_number = randint(1, 10)
print(correct_number)


# Creates home page, prompting user to write '/' and a number (their guess) between 0 and 9
@app.route('/')
def home_route():
    return '<h1>Guess a number between 0 and 9 by adding "/" and your guess to the end of the link.</h1>' \
           '<img src="https://media.giphy.com/media/g7YDlrD5YLqfe/giphy.gif">'


# Guess page that returns an image and the appropriate phrase (high/low/correct)
@app.route("/<int:guess>")
def guess_number(guess):
    if guess < 0 or guess > 10:
        return "<h1 style='color: orange'>Guess is out of bounds. Try Again!</h1>"\
               "<img src='https://media.giphy.com/media/1XgIXQEzBu6ZWappVu/giphy.gif'/>"
    elif guess > correct_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/12bt2k8A5MVhO8/giphy.gif'/>"

    elif guess < correct_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/6lv7cWsF5CP96/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/GwbVjTKRkFgqs/giphy.gif'/>"


# This is necessary to make the app run and give us debugging capabilities, in this case
if __name__ == "__main__":
    app.run(debug=True)
