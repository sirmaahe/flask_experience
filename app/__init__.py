from flask import Flask
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
app.secret_key = '2'

mongo = PyMongo(app)

from app import views
