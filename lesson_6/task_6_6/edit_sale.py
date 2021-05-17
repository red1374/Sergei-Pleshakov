import sys
from utils import check_row, check_value, ROW_LENGTH

if len(sys.argv) < 3:
    print('Not enough parameters!')
else:
    _, row_id, new_value, *other = sys.argv
    new_value = check_value(new_value)
    row_id = check_row(row_id)
    if row_id is None:
        print('Incorrect value for Row ID')
    else:
        with open('bakery.csv', 'r+', encoding='UTF-8') as f:
            f.seek(row_id)
            line = f.read(ROW_LENGTH)
            if line == '':
                print('Incorrect value for Row ID')
            else:
                f.seek(row_id)
                f.write(new_value + '\n')
                print('Item updated!')
