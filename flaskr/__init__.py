from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from flaskr.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from flaskr.models import Image
