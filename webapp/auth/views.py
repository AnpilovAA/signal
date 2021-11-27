from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask import request, jsonify

from db.db_connect import db_session as db
from db_model import Users

blueprint = Blueprint('auth', __name__)

@blueprint.route('/login')
def login():
    arguments = request.args
    username = arguments["username"]
    password = arguments["password"]
    all_info = Users.query.filter_by(username=username,
    password=password).first()
    if username == all_info.username and password == all_info.password:
        check = {
            'status': 'ok'
        }
    else:
        check = {
            'status': 'not ok'
        }
    return jsonify(check)