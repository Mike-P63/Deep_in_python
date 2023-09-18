# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


decimal_number = int(input("Введите положительное десятичное число: "))
print(f'Функция hex = {hex(decimal_number)}')
HEC_DEC_RULES = "0123456789ABCDEF"
hex_decimal_number = " "

while decimal_number > 0:
    n = decimal_number % 16
    hex_dec_rule = HEC_DEC_RULES[n]
    hex_decimal_number = hex_dec_rule + hex_decimal_number
    decimal_number //= 16
print(f'Результат вычисления = Ox{hex_decimal_number}')


# Второй вариант:


# decimal_number = int(input("Введите положительное десятичное число: "))
# print(f'Функция hex = {hex(decimal_number)}')

# def to_hex (number):
#     hex_dec_rules = "0123456789ABCDEF"
#     hex_decimal_number = " "
#     while number > 0:
#         hex_decimal_number = hex_dec_rules[number % 16] + hex_decimal_number
#         number //= 16
#     return '0x' + hex_decimal_number

# print(f'Собственная функция: {to_hex(decimal_number)}')
