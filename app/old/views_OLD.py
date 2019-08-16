from app.objects_OLD import Menu
from app.functions_OLD import function_title
from app.functions_OLD import function_get_user_option


def view_login():
    function_title('LOGIN')
    login = function_get_user_option('Login')
    password = function_get_user_option('Senha')

    menu1.user_login(login, password)

if __name__ == '__main__':
    menu1 = Menu('MENU 1')
    menu2 = Menu('MENU 2')
    menu1_options = [
        {'text': 'Desconectar', 'function': None, 'accesses': [0]},
        {'text': 'menu2', 'function': menu2.display, 'accesses': [0]},
    ]
    menu2_options = [
        {'text': 'Desconectar', 'function': None, 'accesses': [0]},
        {'text': 'menu1', 'function': menu1.display, 'accesses': [0]},
    ]
    menu1.set_options(menu1_options)
    menu2.set_options(menu2_options)

    menu1.display()
