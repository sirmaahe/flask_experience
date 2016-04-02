import os

from flask import Flask
from flask.ext.pymongo import PyMongo
from werkzeug.contrib.fixers import ProxyFix

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://heroku_jzfl2x7q:heroku_jzfl2x7q@ds031883.mlab.com:31883/heroku_jzfl2x7q"

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URL
app.secret_key = 'SECRET KEY'
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)

mongo = PyMongo(app)

from app import views
