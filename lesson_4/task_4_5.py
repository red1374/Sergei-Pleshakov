from utils import print_course
from sys import argv

if argv is None or len(argv) < 2:
    print('Run this script from a command or terminal line')
else:
    print_course(argv[1])
