
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, 
# а значение - кортеж вещей. Ответьте на вопросы:
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, 
# у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен 
# расширяться на любое большее количество друзей.


hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

result = set()
for i in hike.values():
    if result == set():
        result = set(i)
    else:
        result = result & set(i)
# print(result)

only_one = set()
for i in hike.values():
    only_one = set(i)
    for j in hike.values():
        if i==j:
            continue
        else:
            only_one -= set(j)
    # print(only_one)

not_one = set()
for name, i in hike.items():
    for j in hike.values():
        if i==j:
            continue
        elif not not_one:
            not_one = set(j)
        else:
            not_one &= set(j)
    print(name, not_one - set(i))
