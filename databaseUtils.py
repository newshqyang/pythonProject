import mysql.connector


class MyDB(object):
    def __init__(self, host='localhost', user='root', password='0913', db='demo'):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )

    # 从数据库中获取指定账号的密码
    def get_password_from_db(self, username):
        try:
            cursor = self.db.cursor()
            sql = 'SELECT password FROM account WHERE username = "%s";' % username
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            return None

    # 从数据库中获取指定账号的密码
    def create_account(self, username, password):
        try:
            cursor = self.db.cursor()
            sql = 'INSERT INTO account(username, password) VALUES("%s", "%s");' % (username, password)
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            return False
        return True

