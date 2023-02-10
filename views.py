from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


## Start the default website view
@views.route("/")
def home():
    return render_template("index.html", name="guest")

## Pass in a parameter from HTML
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)