import utils

PROJECT_STRUCTURE = 'files/config.yaml'

# dict_config = [
#     ['settings', ['__init__.py', 'dev.py', 'prod.py']],
#     ['mainapp', ['__init__.py', 'models.py', 'views.py']],
#     ['mainapp/templates', []],
#     ['mainapp/templates/mainapp', ['base.html', 'index.html']],
#     ['authapp', ['__init__.py', 'models.py', 'views.py']],
#     ['authapp/templates', []],
#     ['authapp/templates/authapp', ['base.html', 'index.html']]
# ]
#
# with open(PROJECT_STRUCTURE, 'w', encoding="UTF-8") as f_config:
#     f_config.write(dump(dict_config))
#
# with open(PROJECT_STRUCTURE, 'r', encoding="UTF-8") as f_config:
#     print(safe_load(f_config.read()))

project_name = 'project 7.2'
project_config = utils.get_config(PROJECT_STRUCTURE)
if project_config:
    if utils.create_starter(project_name, project_config):
        print(f'Project "{project_name}" has been created!')
    else:
        print(f'Project creating error!')
else:
    print('Config file error!')
