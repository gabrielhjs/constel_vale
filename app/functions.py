from tabulate import tabulate
from hashlib import sha256
from sty import fg, bg, ef, rs

from app.database import db


def function_login(menu):
    global menu
    while True:
        function_title(' UPDATES ')
        updates = [{'date': '15/08/2019', 'title': 'Test', 'text': 'text.........'}]
        for update in updates:
            print(function_indent() + update['date'] + ' - ' + update['title'] + ': ' + update['text'] + ';')

        function_title(' LOGIN ')

        login = function_input_number('Login')
        if not login == -1:
            password = function_input_number('Password')
            if not password == -1:
                password = sha256(str.encode(str(password))).hexdigest()
                verify = db.select(
                    '''
                    SELECT nomefuncionario, nivel, funcionario_coddepartamento, beneficiario_cartao
                    FROM funcionario WHERE codfuncionario = %d AND senha = "%s";
                    ''' % (login, password)
                )
                if len(verify):
                    menu.user.logged(
                        login,
                        verify[0][0],
                        verify[0][1],
                        verify[0][2],
                        verify[0][3],
                        True
                    )
                    function_messages((
                        (2, 'Successfully authenticated'),
                        (2, 'Welcome %s' % menu.user.name),
                    ))
                    return menu.display()
                else:
                    function_messages((
                        (1, 'Invalid authentication'),
                        (0, 'Invalid registration or password'),
                    ))
                    return menu.display()


def function_input_number(text):
    data = input(function_indent() + text + ': ')
    if data.isdigit():
        return int(data)
    else:
        function_messages(((1, 'Enter only numbers'),))
        return -1


def function_exit(call_back):
    pass


def function_messages(messages=()):
    if messages:
        function_title(' WARNINGS ')
        for message in messages:
            if message[0] == 0:
                print(
                    function_indent() + fg.red + ef.italic + ef.bold + 'Error: ' + rs.bold_dim + message[1] +
                    '!' + fg.rs + rs.italic
                )
            elif message[0] == 1:
                print(
                    function_indent() + fg.yellow + ef.italic + ef.bold + 'Warning: ' + rs.bold_dim + message[1] +
                    '!' + fg.rs + rs.italic
                )
            elif message[0] == 2:
                print(
                    function_indent() + fg.green + ef.italic + ef.bold + 'Success: ' + rs.bold_dim + message[1] +
                    '!' + fg.rs + rs.italic
                )
            else:
                print(
                    function_indent() + ef.italic + ef.bold + 'Message: ' + rs.bold_dim + message[1] +
                    '!' + rs.italic
                )


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
    function_title(' EMPLOYERS LIST ')
    data = db.select(
        """
        SELECT codfuncionario, nomefuncionario FROM funcionario ORDER BY nomefuncionario;
        """
    )
    headers = ('MATRÍCULA', 'NOME')
    function_table(data, headers)
    return call_back()
