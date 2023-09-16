# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

fraction_1 = input('Введите первую дробь формата "a/b": ').split('/')
fraction_2 = input('Введите вторую дробь формата "a/b": ').split('/')

imported_1 = Fraction(int(fraction_1[0]), int(fraction_1[1]))
imported_2 = Fraction(int(fraction_2[0]), int(fraction_2[1]))

print(f'Проверка {imported_1 + imported_2}')
print(f'Проверка {imported_1 * imported_2}')

a = int(fraction_1[0])
b = int(fraction_1[1])
c = int(fraction_2[0])
d = int(fraction_2[1])

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def summa_fractions(a, b, c, d):
    x = a*d + b*c
    y = b*d
    z = gcd(x, y)
    return (f'{x//z}/{y//z}')

def multiply_fractions(a, b, c, d):
    num = a * c
    den = b * d
    common_factor = gcd(num, den)
    num //= common_factor
    den //= common_factor
    return (num, den)
product_num, product_den = multiply_fractions(a, b, c, d)

print(f'Собственная функция Сложение: {summa_fractions(a,b,c,d)}')
print(f"Собственная функция Произведение: {product_num}/{product_den}")

