from hashlib import sha256
import sqlite3 as sql
from app.objects import User
from app.views import view_login

DATABASE = '..\\database\\combustivel.db'


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


def controller_login(user, login, password):
    password = str(password)
    password = sha256(str.encode(password)).hexdigest()
    verify = db.select(
        '''
        SELECT nomefuncionario, nivel, funcionario_coddepartamento, beneficiario_cartao
        FROM funcionario WHERE codfuncionario = %d AND senha = "%s";
        ''' % (login, password)
    )
    if len(verify):
        user.logged(
            login,
            verify[0][0],
            verify[0][1],
            verify[0][2],
            verify[0][3],
            True
        )
        return print('logado!')
    else:
        return view_login(user, ('Invalid user!',))
