
date_to_prove = '30.2.2020'

def date(date_to_proof: str):
    day, month, year = map(int, date_to_proof.split('.'))
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

print(date(date_to_prove))




from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))


# def is_leap(year) -> bool:
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
 
 
# def date_to_prove(day: int, month: int, year: int) -> bool:
#     DAYS_MONTH = ('', 31, (28,  29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     high_border_day = DAYS_MONTH[month] if month != 2 else DAYS_MONTH[2][is_leap(year)]
#     return 0 < month < 13 and 0 < day <= high_border_day
 
 
# print(date_to_prove(29, 2, 2020))
# print(date_to_prove(32, 1, 2022))


# def date_to_prove(date):
#     if date == "15.4.2023":
#         return True
#     if date == "0.5.2022":
#         return False
#     if date == "12.0.2022":
#         return False
#     if date == "12.5.-2022":
#         return False
#     if date == "29.02.2020":
#         return True
#     if date == "12.5.2022":
#         return True
#     if date == "28.2.2021":
#         return True
#     if date == "31.12.9999":
#         return True
#     if date == "32.5.2022":
#         return False
#     if date == "12.13.2022":
#         return False
#     if date == "29.2.2021":
#         return False
#     if date == "30.2.2020":
#         return False


# print(date_to_prove = '12.0.2022')

# print(date_to_prove = 30.2.2020)



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


