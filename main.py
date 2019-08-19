from objects import *


if __name__ == "__main__":
    while True:
        user = User()

        user = function_login(user)
        # user.logged(2000542, 'Gabriel', 0, 'tanto faz', 0, True)

        menu_main = Menu(' MAIN MENU ', user)
        menu_queries = Menu(' MENU QUERIES ', user)
        menu_editions = Menu(' EDITIONS MENU ', user)

        menu_main.set_options((
            {
                'text': 'Logout',
                'function': function_logout,
                'accesses': [0],
                'call_back': user
            },
            {
                'text': 'Editions',
                'function': menu_editions.display,
                'accesses': [0],
                'call_back': menu_main.display
            },
            {
                'text': 'Queries',
                'function': menu_queries.display,
                'accesses': [0],
                'call_back': menu_main.display
            },
        ))

        menu_queries.set_options((
            {
                'text': 'Main menu',
                'function': menu_main.display,
                'accesses': [0],
                'call_back': menu_queries.display
            },
            {
                'text': 'Employers',
                'function': query_employers,
                'accesses': [0],
                'call_back': menu_queries.display
            },
        ))

        menu_editions.set_options((
            {
                'text': 'Main menu',
                'function': menu_main.display,
                'accesses': [0],
                'call_back': menu_editions.display
            },
            {
                'text': 'Register new Estar block',
                'function': query_register_block,
                'accesses': [0],
                'call_back': (menu_editions.display, user)
            },
        ))

        menu_main.display()
