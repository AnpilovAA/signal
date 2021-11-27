from flask import Flask, current_app
from flask_login import LoginManager, login_required, current_user
from flask_migrate import Migrate
from webapp.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    from webapp.auth.views import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app