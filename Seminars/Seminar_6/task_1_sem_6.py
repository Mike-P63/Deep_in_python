"""Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: 
нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное 
число в указанных границах и пользователь должен угадать его за заданное число 
попыток. Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь."""

from random import randint

# from sys import argv


def random_number(start_num, stop_num, qty)->bool:
    random_num = randint(start_num, stop_num)
    for _ in range(qty):
        input_num = int(input("Введите число: "))
        if random_num == input_num:
            return True
        elif random_num > input_num:
            print("Число больше")
        else:
            print("Число меньше")
    return False

if __name__ == '__main__':
    print(random_number(2,8,4))
    # a, *b = argv
    # b = list(map(int,b))
    # print(random_number(*b))