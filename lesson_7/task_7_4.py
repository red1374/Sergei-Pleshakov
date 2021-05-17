import os
from collections import defaultdict
from utils import get_dict_key


class DirNotFoundError(Exception):
    def __init__(self, dir_name):
        self.message = f'Directory "{dir_name}" not found!'
        super().__init__(self.message)


def get_dict_key(value=0):
    """
    Get upper border of given value
    :param value: file size
    :return:
    """
    if not value:
        None

    i = 1
    while True:
        if 10 ** i >= value:
            break
        i += 1
    return 10 ** i


def get_dir_stat(dir_path=''):
    """
    Get files count of given directory grouped by file size
    :param dir_path:
    :return:
    """
    if not dir_path:
        return None

    if not os.path.exists(dir_path):
        raise DirNotFoundError(dir_path)

    result = defaultdict(list)

    for dir_tuple in os.walk(dir_path):
        if dir_tuple[2]:
            for file in dir_tuple[2]:
                file_size = os.stat(os.path.join(dir_tuple[0], file)).st_size
                dict_key = get_dict_key(file_size)
                if not result[dict_key]:
                    result[dict_key] = 1
                else:
                    result[dict_key] += 1

    return result


try:
    print(dict(get_dir_stat('files/examples')))
except DirNotFoundError as e:
    print(e.message)
