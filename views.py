from flask import Blueprint, render_template
import os

views = Blueprint(__name__, "views")

## Define the image path folder
img = os.path.join('static', 'images')


## Start the default website view
@views.route("/")
def home():
    file = os.path.join(img, '1.png')
    return render_template("index.html", image=file)

## Pass in a parameter from HTML
@views.route("/moves/<charactername>")
def profile(charactername):
    return render_template("moves.html", name=charactername)