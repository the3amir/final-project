import os
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '5c32252213a16297ab251437f263f8c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

from application import routes