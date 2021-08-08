from flask import request, render_template
from app import app
from models.game import *
from models.player import *

@app.route("/")
def index():
    return render_template("index.html", title="RPS - Home")


@app.route("/<p1choice>/<p2choice>")
def choice(p1choice, p2choice):
    p1 = Player("player", p1choice)
    p2 = Player("opponent", p2choice)
    return render_template("result.html", title="Result - RPS")
