from flask import Flask
from data import db_session, jobs_api
import sqlite3


sqlite3.connect('./db/blogs.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()

