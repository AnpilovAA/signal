import json

from flask import (
    Flask,
    jsonify,
    request,
)
from sqlalchemy.sql.operators import ilike_op

import settings
from db.db_connect import db_session
from db_model import (
    Signals
)

app = Flask(__name__)


@app.route('/')
def index():
    return 'fine'


@app.route('/login')
def login():
    arguments = request.args
    username = arguments['username']
    password = arguments['password']
    check = {
        'status': 'ok'
    }
    return jsonify(check)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        extension = str(file.filename)
        f_name = extension
        file.save(settings.UPLOAD_FOLDER + str(f_name))
        return json.dumps({'filename': f'http://161.35.221.241/img/{f_name}'})


@app.route('/get_signal', methods=['GET'])
def get_signal():
    if request.method == 'GET':
        search_dict = {}
        find_post = db_session.query(
            Signals.id, Signals.image, Signals.updated_at, Signals.topic, Signals.signal,
            Signals.category, Signals.count_likes, Signals.count_dislikes, Signals.author).limit(10)
        if find_post:
            for row in find_post:
                id, image, date, title, text, categories, likes, dislikes, owner = row
                search_dict.setdefault('id', []).append(id)
                search_dict.setdefault('image', []).append(image)
                search_dict.setdefault('date', []).append(date)
                search_dict.setdefault('title', []).append(title)
                search_dict.setdefault('text', []).append(text)
                search_dict.setdefault('categories', []).append(categories.split(','))
                search_dict.setdefault('likes', []).append(likes)
                search_dict.setdefault('dislikes', []).append(dislikes)
                search_dict.setdefault('owner', []).append(owner)
        return search_dict


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        search_dict = {}
        arguments = request.args
        find_post = db_session.query(
            Signals.id, Signals.image, Signals.updated_at, Signals.topic, Signals.signal,
            Signals.category, Signals.count_likes, Signals.count_dislikes, Signals.author).filter(
            ilike_op(Signals.topic, f'%{arguments["q"]}%')).limit(10)
        if find_post:
            for row in find_post:
                id, image, date, title, text, categories, likes, dislikes, owner = row
                search_dict.setdefault('id', []).append(id)
                search_dict.setdefault('image', []).append(image)
                search_dict.setdefault('date', []).append(date)
                search_dict.setdefault('title', []).append(title)
                search_dict.setdefault('text', []).append(text)
                search_dict.setdefault('categories', []).append(categories.split(','))
                search_dict.setdefault('likes', []).append(likes)
                search_dict.setdefault('dislikes', []).append(dislikes)
                search_dict.setdefault('owner', []).append(owner)
        return search_dict


if __name__ == "__main__":
    app.run(host='127.0.0.1')
