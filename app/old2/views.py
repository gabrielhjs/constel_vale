from app.serializers import *
from app.controllers import *


def view_menu_main(messages=()):
    function_messages(messages)
    function_title(' MAIN MENU ')


def view_login(user, outer_messages=()):
    messages = []
    for message in outer_messages:
        messages.append(message)
    while True:
        function_title('UPDATES')
        updates = [{'date': '15/08/2019', 'title': 'Test', 'text': 'text.........'}]
        for update in updates:
            print(function_indent() + update['date'] + ' - ' + update['title'] + ': ' + update['text'] + ';')

        function_messages(messages)
        messages.clear()
        function_title(' LOGIN ')

        login, auth = serializer_int('Login')
        if not auth:
            messages.append('Invalid login')

        else:
            password, auth = serializer_int('Password')
            if not auth:
                messages.append('Invalid password')

            else:
                break

    return controller_login(user, login, password)


if __name__ == "__main__":
    view_login()
