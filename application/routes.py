import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from application import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/all_post", methods=['GET'])
def all_post():
    return render_template('all_post.html')

@app.route("/sections")
def sections():
    return render_template('sections.html', title='sections')

@app.route("/about")
def about():
    return render_template('about.html', title='About')