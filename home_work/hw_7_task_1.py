# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту
# директорию и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах:
# JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
# Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
# и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.

# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать
# результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
# с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.


# import csv
# import json
# import os
# import pickle


# def save_results_to_json(in_dct: dict, path: str, file_name: str) -> None:
#     file_path = os.path.join(path, file_name + '.json')
#     with open(file_path, 'w', encoding='utf-8') as f_out:
#         json.dump(in_dct, f_out, indent=4)


# def save_results_to_csv(in_dct: dict, path: str, file_name: str) -> None:
#     file_path = os.path.join(path, file_name + '.csv')
#     data = [['Basic_path', 'unit_type',  'unit_name', 'unit_size', ' parent_dir', ]]
#     for i_key, i_val in in_dct.items():
#         data.append([i_key, *i_val.values()])
#     with open(file_path, 'w', encoding='utf-8') as f_out:
#         write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
#         write_csv.writerows(data)


# def save_results_to_pickle(in_dct: dict, path: str, file_name: str) -> None:
#     file_path = os.path.join(path, file_name + '.pickle')
#     with open(file_path, 'wb') as f_out:
#         pickle.dump(in_dct, f_out)


# def dct_formatter(total_dct: dict[str, dict[str]],
#                 path: str,
#                 item_name: str,
#                 item_type: str) -> None:
#     if item_type == 'F':
#         total_dct[path] = dict(unit_type='File',
#                 unit_name=item_name,
#                 unit_size=os.path.getsize(os.path.join(path, item_name)),
#                 parent_dir=os.path.split(path)[-1])
#     elif item_type == 'D':
#         total_dct[path] = dict(unit_type='Directory',
#                 unit_name=item_name,
#                 unit_size=count_size(os.path.join(path, item_name)),
#                 parent_dir=os.path.split(os.path.abspath(path))[-1])


# def count_size(count_path: str,
#         dir_size: int = 0) -> float:
#     for sub_item in os.walk(count_path):
#         if sub_item[2]:
#             dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file))
#             for file in sub_item[2]])
#         if sub_item[1]:
#             dir_size += sum([count_size(os.path.join(sub_item[0], subdir))
#             for subdir in sub_item[1]])
#     return dir_size


# def traverse_directory(aim_path: str,
#     total_dct: dict = None) -> dict[str, dict[str]]:
#     if total_dct is None:
#         total_dct = {}
#         basic_path = os.path.split(os.path.abspath(aim_path))
#         dct_formatter(total_dct,
#             os.path.join(*basic_path[:-1]),
#             basic_path[-1],
#             'D')
#     for item in os.listdir(aim_path):
#         check_path = os.path.join(aim_path, item)
#         if os.path.isfile(check_path):
#             dct_formatter(total_dct, aim_path, item, 'F')
#         elif os.path.isdir(check_path):
#             dct_formatter(total_dct, aim_path, item, 'D')
#             traverse_directory(os.path.join(aim_path, item), total_dct)
#     return total_dct


# def dict_printer(in_dict: dict) -> None:
#     for i_key, i_val in sorted(in_dict.items()):
#         print(i_key, end=':')
#         if isinstance(i_val, dict):
#             print()
#             dict_printer(i_val)
#         else:
#             print('\t', i_val)


# def main():
#     directory = 'F:\Deep_in_python\Seminars'
#     result = traverse_directory(directory)
#     save_results_to_json(result, os.getcwd(), 'result')
#     save_results_to_pickle(result, os.getcwd(), 'result')
#     save_results_to_csv(result, os.getcwd(), 'result')


# if __name__ == '__main__':
#     main()


import csv
import json
import os
import pickle


def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "is_file": True,
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})
        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "is_file": False,
                            "name": name,
                            "size_in_bytes": get_size(full_path)})
    with open("output.json", "w") as json_file:
        json.dump(results, json_file)
    with open("output.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(results, pickle_file)
    return json_file, csv_file, pickle_file

directory = 'F:\Deep_in_python\Seminars'
result = traverse_directory(directory)
print(result)


