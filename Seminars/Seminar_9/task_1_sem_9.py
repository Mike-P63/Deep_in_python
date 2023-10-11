# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать
# загаданное число за указанное число попыток.


from typing import Callable


def ran_num(rnd_num, count_num):
    def guess():
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
    return guess


# enigma = ran_num(5, 3)
# print(enigma())

print(ran_num(2,3)())
