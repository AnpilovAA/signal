from flask import Blueprint, request, jsonify
from flask_login import current_user

from db_model import Signals
from db.db_connect import db_session as db

blueprint = Blueprint('signals', __name__)

@blueprint.route('/signals', methods=['POST'])
def signals():
    if current_user.is_authenticated:
        post = request.args
        new_singal = Signals(
            author = current_user.first_name,
            signals = post
        )
        db.add(new_singal)
        db.commit()