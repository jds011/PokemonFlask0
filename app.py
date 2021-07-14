# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import pokemon_choice_message


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')

def index():
    props = {
        'name': 'Blaziken',
        'starts-as': 'Torchic',
        'type': 'fire & fighting'
    }
    return render_template('index.html', props=props)

#get 
#post

@app.route('/secret')
def secret():
    return "You found Mew"

@app.route('/result', methods = ["GET", "POST"])
def result():
    print(request.form["pokemon"])
    user_choice = request.form["pokemon"]
    message = pokemon_choice_message(user_choice)
    return render_template('resultspage.html', message = message)

