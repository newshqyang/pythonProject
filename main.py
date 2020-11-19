import flask
from flask import request
from databaseUtils import MyDB
import json_utils as ju
from flask_cors import *        # 解决跨域问题


server = flask.Flask(__name__)
CORS(server, supports_credentials=True)
db = MyDB()


@server.route('/login', methods=['get', 'post'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')

    pwdFromDB = db.get_password_from_db(username)
    if pwdFromDB is None:
        return ju.failure('账号不存在')
    if password == pwdFromDB:
        return ju.success()
    else:
        print(pwdFromDB)
        print(password)
        return ju.failure('密码错误')


@server.route('/register', methods=['get', 'post'])
def register():
    username = request.values.get('username')
    password = request.values.get('password')

    r = db.create_account(username, password)
    if r:
        return ju.success()
    else:
        return ju.failure('账号已存在')


if __name__ == '__main__':
    server.run(debug=True, port=8080, host='localhost')
    print('服务器启动成功！')
