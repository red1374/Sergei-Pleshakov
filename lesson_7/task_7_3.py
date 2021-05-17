import utils
import os
import shutil

PROJECT_STRUCTURE = 'files/config.yaml'


class CopytreeSourceError(Exception):
    def __init__(self, error='Empty source folder path!'):
        self.message = f'Copytree error: {error}'
        super().__init__(self.message)


class CopytreeDestinationError(Exception):
    def __init__(self, error='Empty destination folder path!'):
        self.message = f'Copytree error: {error}'
        super().__init__(self.message)


def copytree(src_path='', dst_path='', replace_exists_file=False, remove_old_file=False):
    """
    Copy file and folders by source path to destination path
    :param src_path: source path
    :param dst_path: destination path
    :param replace_exists_file: replace files from destination folder if they are exists
    :param remove_old_file:  remove files and folders that were copied
    :return: destination folder
    """
    if not src_path:
        raise CopytreeSourceError
    if not dst_path:
        raise CopytreeDestinationError

    dir_list = os.walk(src_path)
    os.makedirs(dst_path, exist_ok=True)

    for root, dirs, files in dir_list:
        # Skip copied sub folders if they are in destination path
        if root.startswith(dst_path):
            continue

        os.makedirs(root, exist_ok=True)
        for file in files:
            # Remove existing file if necessary
            if os.path.exists(os.path.join(dst_path, file)):
                if replace_exists_file:
                    os.remove(os.path.join(dst_path, file))
                else:
                    continue

            # Copy old file to new location
            shutil.copy2(os.path.join(root, file), dst_path)

        # Remove old files if necessary
        if remove_old_file:
            for file in files:
                os.remove(os.path.join(root, file))
            os.rmdir(root)

    return src_path


def relocate_templates(name='', config_list=False, remove_files=False):
    if config_list is None:
        config_list = []
    if not config_list or not name:
        return None

    template_path = os.path.join(name, 'templates')
    dirs_list = os.walk(name)
    os.makedirs(template_path, exist_ok=True)

    for root, dirs, files in dirs_list:
        if root.find('templates\\') > 0:
            copytree(root, os.path.join(template_path, root.rsplit('\\', maxsplit=1)[-1]), remove_old_file=remove_files)
    return True


project_name = 'project 7.2'
project_config = utils.get_config(PROJECT_STRUCTURE)
if project_config:
    if utils.create_starter(project_name, project_config):
        print(f'Project "{project_name}" was created!')
        try:
            relocate_templates(project_name, project_config)
        except CopytreeSourceError as e:
            print(e.message)
        except CopytreeDestinationError as e:
            print(e.message)
        finally:
            print(f'All template files were copied to {project_name}/templates/ folder')
    else:
        print(f'Project creating error!')
else:
    print('Config file error!')
