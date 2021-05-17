import sys
from utils import check_value

if len(sys.argv) < 2:
    print('Not enough parameters!')
else:
    _, new_value, *other = sys.argv
    new_value = check_value(new_value)

    with open('bakery.csv', 'a', encoding='UTF-8') as f:
        f.write(new_value + '\n')
        print('Item added!')
