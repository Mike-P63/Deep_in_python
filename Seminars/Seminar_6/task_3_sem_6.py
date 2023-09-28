# Добавьте в модуль с загадками функцию, которая принимает на вход строку 
# (текст загадки) и число (номер попытки, с которой она угадана). Функция 
# формирует словарь с информацией о результатах отгадывания. Для хранения 
# используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из 
# защищённого словаря в удобном для чтения виде. Для формирования результатов 
# используйте генераторное выражение.

__all__ = ['mystery','mystery_launch','_archive','show_result']

_result ={}

def mystery(mys:str, answer:list[str], count:int)->int:
    for i in range(1, count+1):
        user_input = input("ответ: ")
        if user_input in answer:
            _archive(mys, 0)
            return i
    _archive(mys, i)
    return 0

def mystery_launch(count):
    mystery_box = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],}
    for key, value in mystery_box.items():
        print(key)
        print(mystery(key, value, count))

def _archive(mys:str, count:int):
    global _result
    _result[mys] = count

def show_result():
    global _result
    print(_result)

if __name__ == '__main__':
    # mys = "'Зимой и летом одним цветом'"
    # answer = ['ель', 'ёлка', 'сосна']
    count = 3

    # print(mystery(mys, answer, count))
    mystery_launch(count)
    show_result()