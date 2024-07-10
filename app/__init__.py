from flask import Flask
from dotenv import load_dotenv
from app.admin import admin
import os

load_dotenv()

from app.extensions import db, migrate, jwt
from config.config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    admin.init_app(app)

    with app.app_context():
        from .models import Person, Vehicle, Officer, Infraction
        from .routes import infractions, reports, auth
        app.register_blueprint(infractions.bp)
        app.register_blueprint(reports.bp)
        app.register_blueprint(auth.auth)

        return app
