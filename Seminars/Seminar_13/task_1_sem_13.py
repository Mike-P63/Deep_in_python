# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

#  С ЛЕКЦИИ:

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


def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
            f'Попробуйте снова')
    return num

if __name__ == '__main__':

    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')


# С семинара:

