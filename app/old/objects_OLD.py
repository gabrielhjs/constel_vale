import sqlite3 as sql
from hashlib import sha256

from app.constants_OLD import *
from app.functions_OLD import function_title
from app.functions_OLD import function_get_user_option
from app.views_OLD import


class DataBase(object):
    def __init__(self, database):
        self.db = sql.connect(database)
        self.cursor = self.db.cursor()
        self.cursor.execute('PRAGMA foreign_keys = ON;')
        self.db.commit()

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def alter(self, query):
        self.cursor.execute(query)
        self.db.commit()


db = DataBase(DATABASE)


class User(object):
    def __init__(self):
        self.user = None
        self.username = None
        self.access = None
        self.department = None
        self.beneficiary_card = None
        self.auth = False

    def user_login(self, login, password):
        password = sha256(str.encode(password)).hexdigest()
        verify = db.select(
            '''
            SELECT nomefuncionario, nivel, funcionario_coddepartamento, beneficiario_cartao
            FROM funcionario WHERE codfuncionario = %d AND senha = "%s";
            ''' % (login, password)
        )
        if len(verify):
            self.user = login
            self.username = verify[0][0]
            self.access = verify[0][1]
            self.department = verify[0][2]
            self.beneficiary_card = verify[0][3]
            self.auth = True


class Menu(User):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.auth_options = []
        self.options = None

    def set_options(self, options):
        self.options = options
        if self.auth:
            for item in range(len(self.options)):
                if self.access in self.options[item]['accesses']:
                    self.auth_options.append(self.options[item])
        else:
            self.auth_options.append({'text': 'Login', 'function': view_login, 'accesses': [0]})

    def display(self):
        function_title(self.title)
        for item in range(len(self.auth_options)):
            print(INDENT + str(item) + ' - ' + self.auth_options[item]['text'])

        option = function_get_user_option()

        if 0 <= option < len(self.auth_options):
            self.auth_options[option]['function']()


if __name__ == '__main__':
    user1 = User()
    user1.user_login(2000542, '2601')
