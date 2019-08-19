import sqlite3 as sql

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


def create_table_bloco():
    query = '''
    CREATE TABLE IF NOT EXISTS estar_bloco (blococod INTEGER PRIMARY KEY);
    '''
    return db.alter(query)


def create_table_folha():
    query = '''
        CREATE TABLE IF NOT EXISTS estar_cartao (
        cartaocod INTEGER PRIMARY KEY,
        cartao_blococod INTEGER NOT NULL REFERENCES estar_bloco(blococod) ON DELETE CASCADE
        );
        '''
    return db.alter(query)


def create_table_cadastro():
    query = '''
    CREATE TABLE IF NOT EXISTS estar_cadastro (
    cadastrocod INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    cadastrodata DATE NOT NULL,
    cadastro_blococod INTEGER NOT NULL REFERENCES estar_bloco(blococod) ON DELETE CASCADE,
    cadastro_codfuncionario INTEGER NOT NULL REFERENCES funcionario(codfuncionario) ON DELETE NO ACTION
    );
    '''
    return db.alter(query)


def create_table_entrega():
    query = '''
    CREATE TABLE IF NOT EXISTS estar_entrega (
    entregacod INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    entregadata DATE NOT NULL,
    entrega_blococod INTEGER NOT NULL REFERENCES estar_bloco(blococod) ON DELETE CASCADE,
    entrega_codfuncionario1 INTEGER NOT NULL REFERENCES funcionario(codfuncionario) ON DELETE NO ACTION,
    entrega_codfuncionario2 INTEGER NOT NULL REFERENCES funcionario(codfuncionario) ON DELETE NO ACTION
    );
    '''
    return db.alter(query)


def create_table_devolucao():
    query = '''
    CREATE TABLE IF NOT EXISTS estar_devolucao (
    devolucaocod INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    devolucaodata DATE NOT NULL,
    devolucao_folhacod INTEGER NOT NULL REFERENCES estar_folha(folhacod) ON DELETE CASCADE,
    devolucao_codfuncionario1 INTEGER NOT NULL REFERENCES funcionario(codfuncionario) ON DELETE NO ACTION,
    devolucao_codfuncionario2 INTEGER NOT NULL REFERENCES funcionario(codfuncionario) ON DELETE NO ACTION
    );
    '''
    return db.alter(query)


if __name__ == '__main__':
    create_table_bloco()
    create_table_cadastro()
    create_table_entrega()
    create_table_devolucao()
    create_table_folha()
