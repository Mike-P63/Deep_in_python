import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())


import os
import shutil
from pathlib import Path

# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

# os.makedirs('dir/other_dir/new_os_dir')

# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# shutil.rmtree('dir')
# shutil.rmtree('some_dir')

# print(os.listdir())

# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
#     print(f'{obj = }')
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
