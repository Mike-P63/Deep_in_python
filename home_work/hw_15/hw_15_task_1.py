import argparse
import logging

FORMAT = '{levelname}, {asctime}, {msg}'

logging.basicConfig(format = FORMAT, style='{', filename = "myfunc_2.log", filemode ="w", encoding="utf-8", level=logging.ERROR)
logger = logging.getLogger(__name__)

def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}")
        return None
    return wrapper

@ log_dec
def rucksack_max_wheith(x, n):
    possible_items = []
    for item, weight in x.items():
        if weight <= n:
            possible_items.append(item)
            n -= weight
    return possible_items


ITEMS = {'Топор': 1, 'Вода': 3, 'Консервы': 6, 'Одежда': 4, 'Палатка': 2, 'Котелок': 5 }

MAX_WHEITH = 0,5


print(f'В рюкзак поместятся вещи: {rucksack_max_wheith(ITEMS, MAX_WHEITH)}')


