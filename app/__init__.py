from flask import Flask
from flask.ext.pymongo import PyMongo
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.secret_key = 'SECRET KEY'
app.wsgi_app = ProxyFix(app.wsgi_app)

mongo = PyMongo(app)

from app import views
