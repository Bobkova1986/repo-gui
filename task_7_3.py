import os
from shutil import copytree


def copy_dir():
    dir_src = 'my_project'
    dir_dst = 'templates'

    for root, dirs, files in os.walk(dir_src):
        if root.find(dir_dst) > 0:
            copytree(os.path.join(root), dir_dst, dirs_exist_ok=True)


copy_dir()