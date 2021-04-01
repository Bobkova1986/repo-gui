import os
main_dir = 'my_project'
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']

dir_path = os.path.join(main_dir)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
for i in dir_list:
    dirs_path = os.path.join(main_dir, i)
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)
