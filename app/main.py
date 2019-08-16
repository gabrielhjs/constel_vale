from app.objects import *


if __name__ == "__main__":
    menu_main = Menu(' MAIN MENU ')
    menu_queries = Menu(' MENU QUERIES ')
    menu_main.logged(2000542, 'Gabriel', 0, 'tanto faz', 0, True)
    menu_queries.logged(2000542, 'Gabriel', 0, 'tanto faz', 0, True)
    menu_main.set_options((
        {'text': 'Exit', 'function': function_exit, 'accesses': [0]},
        {'text': 'Queries', 'function': menu_queries.display, 'accesses': [0]},
    ))
    menu_queries.set_options((
        {'text': 'Main menu', 'function': menu_main.display, 'accesses': [0]},
        {'text': 'Employers', 'function': query_employers, 'accesses': [0]},
    ))
    menu_main.display()



