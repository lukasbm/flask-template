import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'jonas ist ein kek'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'home.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app import routes
