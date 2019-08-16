from app.constants_OLD import *
from app.objects_OLD import User


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


def function_get_user_option(text):
    print()
    option = input(INDENT + text + ': ')
    if option.isdigit():
        return int(option)
    else:
        return -1


if __name__ == '__main__':
    pass
