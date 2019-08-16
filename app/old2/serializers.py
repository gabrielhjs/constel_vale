from app.functions import *


def serializer_int(text):
    data = input(function_indent() + text + ': ')
    if data.isdigit():
        return int(data), True
    else:
        return -1, False
