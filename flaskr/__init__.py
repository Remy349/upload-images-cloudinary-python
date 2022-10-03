import os
import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

if not Config.SQLALCHEMY_DATABASE_URI:
    raise RuntimeError("DATABASE_URL is not set!")
else:
    print("DATABASE_URL is ok!!!!")

app.config.from_object(Config)

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from flaskr import routes
from flaskr import models

