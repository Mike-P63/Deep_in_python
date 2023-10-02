# Создайте функцию для сортировки файлов по директориям: видео, изображения, 
# текст и т.п. Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, 
# которые не подошли для сортировки.


# import os
# import pathlib


# def sort_files(path):
#     os.chdir(path)
#     files = os.listdir()
#     ext = {}
#     for i in path.iterdir():
#         if i .is_file():
#             ext[i.suffix] = ext.get(i.suffix,[]) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for file in value:
#             try:
#                 file.replace(path/key)
#             except PermissionError:
#                 continue

            

# sort_files(pathlib.Path(r'F:\Deep_in_python\Seminars\Seminar_7\tests'))



import os
import pathlib


def sort_files(path):
    os.chdir(path)
    ext = {}
    for i in path.iterdir():
        if i.is_file():
            ext[i.suffix] = ext.get(i.suffix, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
        for file in value:
            try:
                file.replace(path/key/file.name)
            except PermissionError:
                continue


sort_files(pathlib.Path(r"D:\обучение\python\python part 2\sem7\testt"))










# def sort_files(path):
#     os.chdir(path)
#     files = os.listdir()
#     ext = {}
#     for i in files:
#         *_, extension = i.split('.')
#         ext[extension] = ext.get(extension,[]) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for i in value:
#             os.replace(i, key)

# sort_files(r'F:\Deep_in_python\Seminars\Seminar_7\tests')


