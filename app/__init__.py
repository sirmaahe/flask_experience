import os

from flask import Flask
from flask.ext.pymongo import PyMongo
from werkzeug.contrib.fixers import ProxyFix

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:31883"

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URL
app.secret_key = 'SECRET KEY'
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)

mongo = PyMongo(app)

from app import views
