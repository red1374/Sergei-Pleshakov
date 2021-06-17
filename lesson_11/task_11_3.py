class WrongListValueError(Exception):
    def __init__(self, value):
        self.txt = f'List has wrong item value: \033[31m{value}\033[0m!'


input_value = input('Insert digit or "*" for exit \n')
digits_list = []
while input_value != '*':
    try:
        try:
            input_value = float(input_value)
        except ValueError:
            raise WrongListValueError(input_value)
    except WrongListValueError as e:
        print(e.txt)
    else:
        digits_list.append(float(input_value))

    input_value = input('Insert digit or "*" for exit \n')

print(digits_list)
