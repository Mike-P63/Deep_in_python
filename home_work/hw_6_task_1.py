


def date_to_prove(date):
    string_num = str(date)
    print(string_num)
    day, month, year = map(int, string_num.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif 1 <= day <= 28 + is_leap_year(year):
            return True
        else:
            return False
    return False

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(date_to_prove ("29.2.2024"))






# gjcktlytt

# import os
# import pathlib


# def sort_files(path):
#     os.chdir(path)
#     ext = {}
#     for i in path.iterdir():
#         if i.is_file():
#             ext[i.suffix] = ext.get(i.suffix, []) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for file in value:
#             try:
#                 file.replace(path/key/file.name)
#             except PermissionError:
#                 continue


# sort_files(pathlib.Path(r"D:\обучение\python\python part 2\sem7\testt"))

# def sort_files(path):
#     os.chdir(path)
#     files = os.listdir()
#     ext = {}
#     for i in files:
#         *_, extention = i.split(".")
#         ext[extention] = ext.get(extention, []) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for i in value:
#             os.replace(i, f"{key}\\{i}")

# sort_files(r"python part 2\sem7\testt")


