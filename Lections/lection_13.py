# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')



# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#             f'Попробуйте снова')
#     return num

# if __name__ == '__main__':

#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


# def hundred_div_num(text: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(text))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#             f'Попробуйте снова')
#         except ZeroDivisionError as e:
#             div = float('inf')
#             break
#     return num, div

# if __name__ == '__main__':
#     n, d = hundred_div_num('Введите целый делитель: ')
#     print(f'Результат операции: "100 / {n} = {d}"')

# MAX_COUNT = 5
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#         break
# print(f'{result = }')


# def get(text: str = None) -> int:
#     num = None
#     try:
#         num = int(input(text))
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#     finally:
#         return num if isinstance(num, int) else 1

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     try:
#         print(f'100 / {number} = {100 / number}')
#     except ZeroDivisionError as e:
#         print(f'На ноль делить нельзя. Получим {e}')

class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом.Используйте int или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age

user = User('Яков', '-12')

