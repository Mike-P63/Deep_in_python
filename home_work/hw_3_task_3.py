# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут
# в рюкзак передав его максимальную грузоподъёмность. Достаточно
# вернуть один допустимый вариант.


def rucksack_max_wheith(ITEMS, MAX_WHEITH):
    possible_items = []
    for item, weight in ITEMS.items():
        if weight <= MAX_WHEITH:
            possible_items.append(item)
            MAX_WHEITH -= weight
    return possible_items


ITEMS = {'Топор': 1, 'Вода': 3, 'Консервы': 4, 'Одежда': 3, 'Палатка': 2, 'Котелок': 1 }
MAX_WHEITH = 10
print(f'В рюкзак поместятся вещи: {rucksack_max_wheith(ITEMS, MAX_WHEITH)}')