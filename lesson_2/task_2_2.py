# Checks if value type is integer
def is_integer(_str):
    if _str is False:
        return False

    if _str.isdigit():
        return True
    elif _str[1:].isdigit() and (_str[0:1] == '+' or _str[0:1] == '-'):
        return True

    return False


# Add zeros to integer digits if it needed
def add_zeros(list_item):
    if list_item[0] == '-' or list_item[0] == '+':
        digits = list_item[1:]
        digits_sign = list_item[0:1]
    else:
        digits = list_item
        digits_sign = ''

    return digits_sign + f'{int(digits):02d}'


# Prints list by items in one row
def print_string(_list):
    if _list is False:
        return False

    for ids in range(len(_list)):
        if (_list[ids] == '"' and is_integer(_list[ids + 1])) or is_integer(_list[ids]):
            ends = ''
        else:
            ends = ' '

        print(_list[ids], end=ends)


# Add quotes to the given _list around a integer value
def add_quotes(_index, _list):
    _list.insert(_index, '"')
    _list.insert(_index + 2, '"')

    return 2


weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_id = 0
for idx in range(len(weather_list)):
    if is_integer(weather_list[new_id]):
        weather_list[new_id] = add_zeros(weather_list[new_id])
        new_id += add_quotes(new_id, weather_list)

    new_id += 1

print_string(weather_list)
