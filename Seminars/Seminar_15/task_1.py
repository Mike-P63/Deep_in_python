# Напишите программу, которая использует модуль 
# logging для вывода сообщения об ошибке в файл. 
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename = "myfunc.log", filemode ="w", encoding="utf-8", level=logging.ERROR)



def my_func(storage, key, value = None):
    try:
        return storage[key]
    except KeyError:
        logging.error(f"No key {key} in slovar {storage}")
        return value
    

f = {'f' : '1', 'd' : '3', 's' : '5'}

print(my_func(f, 'a', 23))