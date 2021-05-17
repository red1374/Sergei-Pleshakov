import json
import yaml
import os

yaml.dump
# class ProjectConfigError(Exception):
#     def __init__(self, error='File not found!'):
#         self.message = f'Project config file error: {error}'
#         super().__init__(self.message)

# class CreateProjectError(Exception):
#     def __init__(self, name='empty value'):
#         self.message = f'"{name}" is wrong project name'
#         super().__init__(self.message)


def get_config(file_name):
    """
    Get parameters list from configuration file
    :param file_name: file name
    :return:
    """
    if not file_name or not os.path.exists(file_name):
        return None

    ext = file_name.rsplit('.', maxsplit=1)[-1].lower()
    with open(file_name, 'r', encoding="UTF-8") as f_config:
        if ext == 'yaml':
            return yaml.safe_load(f_config)
        elif ext == 'json':
            return json.load(f_config)
        else:
            return None


def create_starter(name='my_project', config_list=''):
    """
    Create project file structure from config_list parameters
    :param name: project name
    :param config_list: information about project files structure
    :return:
    """
    if not name or config_list is None or not len(config_list):
        return None

    os.makedirs(name, exist_ok=True)

    for root, files in config_list:
        os.makedirs(os.path.join(name, root), exist_ok=True)
        for file in files:
            fil_path = os.path.join(name, root, file)
            if not os.path.exists(fil_path):
                with open(fil_path, 'w', encoding="UTF-8") as new_f:
                    new_f.write('')

    return True


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

