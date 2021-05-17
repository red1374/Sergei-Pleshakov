import os
from utils import get_dict_key
from collections import defaultdict


class DirNotFoundError(Exception):
    def __init__(self, dir_name):
        self.message = f'Directory "{dir_name}" not found!'
        super().__init__(self.message)


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
                file_stat = os.stat(os.path.join(dir_tuple[0], file))
                dict_key = get_dict_key(file_stat.st_size)
                ext = file.rsplit('.', maxsplit=1)[-1]

                if not result[dict_key]:
                    result[dict_key] = [1, {ext}]
                else:
                    result[dict_key][0] += 1
                    result[dict_key][1].add(ext)

    if len(result.items()):
        result = {key: tuple([value[0], list(value[1])]) for key, value in result.items()}

    return result


try:
    print(dict(get_dir_stat('files/examples')))
except DirNotFoundError as e:
    print(e.message)
