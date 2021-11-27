from flask import Flask, current_app
from flask_migrate import Migrate

from webapp.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    return app