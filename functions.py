from tabulate import tabulate
from hashlib import sha256
from sty import fg, bg, ef, rs

from database import db


def function_login(user):
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
                    user.logged(
                        login,
                        verify[0][0],
                        verify[0][1],
                        verify[0][2],
                        verify[0][3],
                        True
                    )
                    function_messages((
                        (2, 'Successfully authenticated'),
                        (2, 'Welcome %s' % user.name),
                    ))
                    return user
                else:
                    function_messages((
                        (1, 'Invalid authentication'),
                        (0, 'Invalid registration or password'),
                    ))
                    return user


def function_logout(user):
    user.auth = False
    return user


def function_input_number(text):
    data = input(function_indent() + text + ': ')
    if data.isdigit():
        return int(data)
    else:
        function_messages(((1, 'Enter only numbers'),))
        return -1


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
                    function_indent() + fg.da_green + ef.italic + ef.bold + 'Success: ' + rs.bold_dim + message[1] +
                    '!' + fg.rs + rs.italic
                )
            else:
                print(
                    function_indent() + ef.italic + ef.bold + 'Message: ' + rs.bold_dim + message[1] +
                    '!' + rs.italic
                )
            print('\033[31m'+'Isto eh vermelho'+'\033[0;0m')


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


def query_register_block(call_back):
    user = call_back[1]
    call_back = call_back[0]
    while True:
        function_title(' REGISTER A NEW ESTAR BLOCK ')
        block = controller_block_card('Enter Estar block code')
        if not block:
            continue
        if block == -1:
            function_messages((
                (2, 'Operation canceled'),
            ))
            return call_back()
        block_existent = db.select(
            """
            SELECT blococod FROM estar_bloco WHERE blococod = %d;
            """ % block
        )
        if not len(block_existent):
            card_ini = controller_block_card('Enter code of first Estar block card')
            if not card_ini:
                continue
            if card_ini == -1:
                function_messages((
                    (2, 'Operation canceled'),
                ))
                return call_back()
            card_fin = controller_block_card('Enter code of last Estar block card')
            if not card_fin:
                continue
            if card_fin == -1:
                function_messages((
                    (2, 'Operation canceled'),
                ))
                return call_back()
            if card_ini <= card_fin:
                messages = []
                if (card_fin - card_ini) != 10:
                    messages.append(
                        (1, 'This block does not contain 10 cards'),
                    )
                db.alter(
                    """
                    INSERT INTO estar_bloco (blococod) VALUES (%d);
                    """ % block
                )
                for i in range(card_ini, card_fin + 1):
                    db.alter(
                        """
                        INSERT INTO estar_cartao (cartaocod, cartao_blococod) VALUES (%d, %d);
                        """ % (i, block)
                    )
                db.alter(
                    """
                    INSERT INTO estar_cadastro (cadastrodata, cadastro_blococod, cadastro_codfuncionario) VALUES(
                    datetime("now","localtime"), %d, %d
                    )
                    """ % (block, user.login)
                )
                messages.append(
                    (2, 'Estar block successfully registered'),
                )
                function_messages(messages)
                return call_back()
            else:
                function_messages((
                    (0, 'First card code must be less than or equal to last card code'),
                ))
        else:
            function_messages((
                (0, 'This Estar block has already been registered in the system'),
            ))


def controller_block_card(text):
    block1 = input(function_indent() + text + ': ')
    if block1 == '0':
        return -1
    if block1.isdigit():
        if len(block1) == 9:
            block2 = input(function_indent() + 'Confirm the code: ')
            if block2 == '0':
                return -1
            if block1 == block2:
                block1 = int(block1)
                return block1
            else:
                function_messages((
                    (0, 'The codes do not match'),
                ))
                return False
        else:
            function_messages((
                (0, 'The code must contain 9 digits'),
            ))
            return False
    else:
        function_messages((
            (0, 'Enter only numbers'),
        ))
        return False
