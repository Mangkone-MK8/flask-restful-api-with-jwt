from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from restful_api.config import Config
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()

ma = Marshmallow()

jwt = JWTManager()

migrate = Migrate()


def configure_database(app):
    @app.before_first_request
    def create_default():
        with app.app_context():
            db.create_all()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(Config)
    

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    configure_database(app)

    from restful_api.user.route import users
    app.register_blueprint(users)

   

    return app
