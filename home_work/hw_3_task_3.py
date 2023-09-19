# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут
# в рюкзак передав его максимальную грузоподъёмность. Достаточно
# вернуть один допустимый вариант.


def rucksack_max_wheith(x, n):
    possible_items = []
    for item, weight in x.items():
        if weight <= n:
            possible_items.append(item)
            n -= weight
    return possible_items


ITEMS = {'Топор': 1, 'Вода': 3, 'Консервы': 2, 'Одежда': 3, 'Палатка': 2, 'Котелок': 1 }
MAX_WHEITH = 10
print(f'В рюкзак поместятся вещи: {rucksack_max_wheith(ITEMS, MAX_WHEITH)}')