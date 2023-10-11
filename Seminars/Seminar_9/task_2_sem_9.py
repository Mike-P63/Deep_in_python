# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку
# числа в диапазоны [1, 100] и [1, 10]. Если не входят, вызывать
# функцию со случайными числами из диапазонов.



from random import randint
from typing import Callable
from functools import wraps

def game_decor(func: callable):
    @wraps(func)
    def wrapper(rnd_num, count_num):
        if not 1 <= rnd_num <=100:
            rnd_num = randint(1,100)
        if not 1 <= count_num <=10:
            count_num = randint(1,10)
        result = func(rnd_num, count_num)
        return result
    return wrapper

@game_decor
def guess(rnd_num, count_num):
        for i in range(count_num):
            input_num = int(input("Введите число для угадывания: "))
            if input_num > rnd_num:
                print("Число меньше загаданного")
            elif input_num < rnd_num:
                print("Число больше загаданного")
            else:
                print(rnd_num)
                return True
        return False

if __name__ == "__main__":
    guess(2,3)

