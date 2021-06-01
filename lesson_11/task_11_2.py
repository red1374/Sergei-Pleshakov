import random


class ZeroDivisionNewError(Exception):
    def __init__(self):
        self.txt = f'Can\'t dived on zero!'


input_value = input('Insert divider digit or "*" for exit \n')
while input_value != '*':
    if input_value == '*' or input_value.isdigit():
        digit = random.randint(15, 176)
        try:
            if int(input_value) != 0:
                res = digit / int(input_value)
            else:
                raise ZeroDivisionNewError
        except ZeroDivisionNewError:
            print('You cant divide8 on zero!')
        else:
            print(digit, '/', input_value, '=', res)
    else:
        print('Input digit, please!')

    input_value = input('Insert divider digit or "*" for exit \n')
