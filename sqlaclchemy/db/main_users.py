from flask import Flask
from data import db_session, jobs_api
from data.users import User
import sqlite3


sqlite3.connect('./db/blogs.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = "21"
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief1@mars.org'

    user2 = User()
    user2.surname = "Mike"
    user2.name = "Harrison"
    user2.age = "25"
    user2.position = 'astronaut'
    user2.speciality = 'researcher'
    user2.address = 'module_2'
    user2.email = 'mike_love@mars.org'

    user3 = User()
    user3.surname = "Tom"
    user3.name = "Bag"
    user3.age = "28"
    user3.position = 'tourist'
    user3.speciality = 'nothing'
    user3.address = 'module_3'
    user3.email = 'tom_just@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
