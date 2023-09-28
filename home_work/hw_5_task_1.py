# Напишите функцию get_file_info, которая принимает 
# на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.

# import os

# file_path = "C:/Users/User/Documents/example.txt"

# def get_file_info(file_path):
#     file_path, file_extension = os.path.splitext(file_path)
#     dirname, filename = os.path.split(file_path)
#     return (dirname, filename, file_extension)

# print(get_file_info(file_path))


# def get_file_info(abs_path: str) -> tuple:
#     result = []
#     for divine in ['.', ['\\', '/']]:
#         for i in range(len(abs_path) - 1, -1, -1):
#             if abs_path[i] in divine:
#                 result.insert(0, abs_path[i+1:])
#                 abs_path = abs_path[:i]
#                 break
#     result.insert(0, abs_path)
#     return tuple(result)

# print(get_file_info(file_path))

import os

# def get_file_info(file_path):
#     file_path, file_extension = os.path.splitext(file_path)
#     dirname, filename = os.path.split(file_path)
#     return (dirname, filename, file_extension)

# print(get_file_info(file_path = "C:/Users/User/Documents/example.txt"))


# file_path = "C:/Users/User/Documents/example.txt"

# def fun(file_path: str) -> tuple:
#     path, filename = os.path.split(file_path)
#     name, extension = filename.split('.')
#     return path, name, extension

# print(f'Исходная строка: {file_path} \nКортеж из пути: {fun(file_path)}')

import os

file_path = "C:/Users/User/Documents/example.txt"

def get_file_info(path):
    *path_el, name_ext = path.split('/')
    name, extension = name_ext.split('.')
    return '/'.join(path_el) + '/', name, extension

print(get_file_info(file_path))


# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)

# print(get_file_info(file_path))