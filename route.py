import os
import secrets
import flask
from application.models import User, Post, Img

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')