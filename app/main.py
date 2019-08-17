from app.objects import *


if __name__ == "__main__":
    user = User()
    #user.logged(2000542, 'Gabriel', 0, 'tanto faz', 0, True)
    menu_main = Menu(' MAIN MENU ', user)
    menu_queries = Menu(' MENU QUERIES ', user)

    menu_main.set_options((
        {'text': 'Exit', 'function': function_exit, 'accesses': [0], 'call_back': menu_main.display},
        {'text': 'Queries', 'function': menu_queries.display, 'accesses': [0], 'call_back': menu_main.display},
    ))

    menu_queries.set_options((
        {'text': 'Main menu', 'function': menu_main.display, 'accesses': [0], 'call_back': menu_queries.display},
        {'text': 'Employers', 'function': query_employers, 'accesses': [0], 'call_back': menu_queries.display},
    ))

    menu_main.display()
