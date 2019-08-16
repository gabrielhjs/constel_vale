from tabulate import tabulate

from app.database import db


def function_login(call_back):
    pass


def function_exit(call_back):
    pass


def function_messages(messages=()):
    if messages:
        function_title(' WARNINGS ')
        for message in messages:
            print(function_indent() + 'Warning: ' + message + '!')


def function_title(title=''):
    length = 50
    symbol = '-'
    side = symbol * (length - (len(title) // 2))
    print()
    if not len(title) % 2:
        print(side + '-' + title + side, sep='')
    else:
        print(side + title + side, sep='')
    print()


def function_indent():
    return '    '


def function_table(data, headers):
    return print(
        tabulate(
            data,
            headers=headers,
            tablefmt="psql",
            stralign="left",
            numalign="center",
        )
    )


def query_employers(call_back):
    data = db.select(
        """
        SELECT codfuncionario, nomefuncionario FROM funcionario ORDER BY nomefuncionario;
        """
    )
    headers = ('MATRÍCULA', 'NOME')
    function_table(data, headers)
    return call_back()
