# Напишите функцию принимающую на вход только ключевые параметры 
# и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его 
# строковое представление. 
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def modified_dict(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict

print(modified_dict(name = 'Иван', surname = 'Иванов', age = 22))

