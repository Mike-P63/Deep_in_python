# Создайте модуль с функцией внутри. Функция получает на вход загадку, 
# список с возможными вариантами отгадок и количество попыток на угадывание. 
# Программа возвращает номер попытки, с которой была 
# отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. Функция в цикле 
# вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ['mystery', 'mystery_launch']

def mystery(mys:str, answer:list[str], count:int)->int:
    for i in range(1, count+1):
        user_input = input("ответ: ")
        if user_input in answer:
            return i
    return 0

def mystery_launch(count):
    mystery_box = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],}
    for key, value in mystery_box.items():
        print(key)
        print(mystery(key, value, count))


if __name__ == '__main__':
    # mys = "'Зимой и летом одним цветом'"
    # answer = ['ель', 'ёлка', 'сосна']
    count = 3

    # print(mystery(mys, answer, count))
    mystery_launch(count)