import sys
from utils import print_rows, check_row

_, *other = sys.argv

if len(other) == 0:
    # Output all list items
    print_rows()
elif len(other) >= 1:
    if not other[0].isdigit():
        print('Wrong input parameters!')
    else:
        start_row = int(other[0])
        end_row = 0

        if len(other) >= 2 and other[1].isdigit():
            end_row = int(other[1])

        # Output items from given position to the end of list if end_row is empty
        start_position = check_row(start_row)
        end_position = check_row(end_row)

        print_rows(start_position, end_position)
