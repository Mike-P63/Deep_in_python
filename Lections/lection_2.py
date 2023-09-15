# import sys
import decimal

# a = "Hello"
# print(type(a), id(a))

# text = str(input('Введите текст из 5 слов: '))
# print(text, id(text), type(text), hash(text))

# print(dir("Hello world!"))
# help()

# x = 162
# print(bin(x), oct(x), hex(x))

# data = 42.3
# num = 6
# print(isinstance(data, (int,float,complex)))
# print(data is num)

# a: int = 42
# b: float = float(input("Enter: "))
# print(a/b)

# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP


# LIMIT = 120
# ATTENION = 'Внимание! '
# name = input('Твое имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENION + 'Хоть тебе и осталось ' + str(100 - age) +\
#     " До ста лет но длина строки не более " + str(LIMIT) + " символов"
# print(text)

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_355')
print(pi)
# MIN_RANGE = 0
# MAX_RANGE = 100000
# MIN_PRIME_NUM = 2

# def is_prime(n):
#     if n <= 1:
#         return "Вы ввели некорректное число"
#     if n == MIN_PRIME_NUM:
#         return "Число, введенное вами - простое"
#     for i in range(MIN_PRIME_NUM ,n):
#         if n % i == 0:
#             return "Число, введенное Вами - составное"
#         else:
#             return "Число, введенное вами - простое"

# n = int(input(f'Введите целое число в диапазоне от {MIN_RANGE} до {MAX_RANGE}: '))
# print(is_prime(n))