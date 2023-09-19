# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


my_list = (2,2,3,3,4,5,6,6,7,7,8,9)

def only_double(my_list):
    return list(set(filter(lambda x: my_list.count(x) > 1, my_list)))

print(f'Дублирующиеся элементы в списке: {only_double(my_list)}')


# Второй вариант решения:

my_list = [1, 2, 3, 2, 1, 4, 7, 5, 6, 7, 10, 12]
my_list_filter = []

for el in my_list:
    if my_list.count(el) > 1 and el not in my_list_filter:
        my_list_filter.append(el)

print("Дублирующиеся элементы в списке: ", my_list_filter)
