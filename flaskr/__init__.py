from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

if not Config.SQLALCHEMY_DATABASE_URI:
    raise RuntimeError("DATABASE_URI is not set!")
else:
    print("DATABASE_URI is ok!!!!")

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from flaskr import routes
from flaskr import models

