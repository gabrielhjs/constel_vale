from app.functions import *


class User:
    def __init__(self):
        self.login = None
        self.name = None
        self.access = None
        self.department = None
        self.beneficiary_card = None
        self.auth = False

    def logged(self, login, name, access, department, beneficiary_card, auth):
        self.login = login
        self.name = name
        self.access = access
        self.department = department
        self.beneficiary_card = beneficiary_card
        self.auth = auth


class Menu(User):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.auth_options = []
        self.options = None
        self.indent = '   '

    def set_options(self, options):
        self.options = options
        if self.auth:
            for item in range(len(self.options)):
                if self.access in self.options[item]['accesses']:
                    self.auth_options.append(self.options[item])
        else:
            self.auth_options.append(
                {'text': 'Exit', 'function': function_exit, 'accesses': [0]},
            )
            self.auth_options.append(
                {'text': 'Login', 'function': function_login, 'accesses': [0]},
            )

    def display(self, *args):
        function_title(self.title)
        for item in range(len(self.auth_options)):
            print(self.indent + str(item) + ' - ' + self.auth_options[item]['text'])

        self.get_user_option()

    def get_user_option(self):
        print()
        option = input(self.indent + 'Choose an option: ')
        if option.isdigit():
            option = int(option)
        else:
            option = -1

        if 0 <= option < len(self.auth_options):
            return self.auth_options[option]['function'](self.display)
        else:
            function_messages(('Invalid option',))
            return self.display()
