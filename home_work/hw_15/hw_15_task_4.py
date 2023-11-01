# Работаю с логгированием и вводом в командную строку используя функцию parser_func

import argparse
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename = "myfunc_5.log", filemode ="w", encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def get_number(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число, систему исчисления и возвращает его  строковое представление.
    :param number: само число
    :param mod: система исчисления
    :return: строковое представление
    """
    result = ''
    if mod < 0:
        logger.error(f'Система исчисления {mod} не существует')
        return float('inf')
    while number != 0:
        try:
            result = str(number % mod) + result
            number //= mod
        except ZeroDivisionError as e:
            logger.error(f'Система исчисления {mod} не существует')
            return float('inf')
    logger.info(f'{number}, {mod} = {result}')
    return result

#  работа через функцию:

def parser_func():
    parser = argparse.ArgumentParser(description='Получаем аргументы из строки')
    parser.add_argument('--number')
    parser.add_argument('--mod', default=10)
    args = parser.parse_args()
    print(args)
    return get_number(int(args.number), int(args.mod))

parser_func()

# if __name__ == '__main__':
#     print(get_number(1234123, 2))
#     print(get_number(1234123, 0))
#     print(get_number(1234123, -2))
    

# Ввод в командной строке: python Home_Work/hw_15/hw_15_task_4.py --number 1234123 --mod -2


# В файле myfunc_5.log:
# ERROR - 2023-11-01 14:32:09,213 - Система исчисления -2 не существует
