ROW_LENGTH = 20


def check_value(_value):
    """
    Check input value length
    :param _value: new value string
    :return: result value
    """
    if len(_value) > ROW_LENGTH:
        val = input(f'Value has more than {ROW_LENGTH} characters long.'
                    f' Print "y" to shrink it to {ROW_LENGTH} characters or print a new value:\n')
        if val == 'y':
            _value = _value[:ROW_LENGTH]
        else:
            _value = val

    _value += (' ' * (ROW_LENGTH - len(_value)))

    return _value


def print_rows(_start=0, _end=0):
    """
    Print row from a file
    :param _start: first row number
    :param _end: last row number
    :return: void
    """
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        # Go to calculated position at file
        if _start > 0:
            f.seek(_start)

        current_row = _start
        for line in f:
            if len(line.strip()):
                print(line.strip())
            else:
                continue

            current_row += ROW_LENGTH
            if _end and current_row >= _end:
                break


def check_row(row_id):
    if row_id is None or int(row_id) < 1:
        return None

    return (int(row_id) - 1) * (ROW_LENGTH + 2)

