import utils

PROJECT_STRUCTURE = 'files/config.json'

# project_dirs = [
#     ['settings', ['tmp5.txt']], ['mainapp', ['__init__.py']], ['adminapp', []], ['authapp', []], ['authapp/subdir', []]
# ]
# with open(PROJECT_STRUCTURE, "w", encoding="UTF-8") as f:
#     json.dump(project_dirs, f)

project_name = 'project 7.1'
project_config = utils.get_config(PROJECT_STRUCTURE)
if project_config:
    if utils.create_starter(project_name, project_config):
        print(f'Project "{project_name}" has been created!')
    else:
        print(f'Project creating error!')
else:
    print('Config file error!')
