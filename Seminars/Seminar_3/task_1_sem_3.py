# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.

# lst=[3,7,13,666,2,7,20,13,3]
# print(list(filter(lambda x: lst.count(x) == 1, lst)))


numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)



numbers = [23, 23, 38, 38, 66, 66, 90]

def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
print(get_unique_numbers(numbers))

print()

a = [2,2,3,3,4,4,99]
res = []
for el in a:
    if el not in res:
        res.append(el)
print(res)






# numbers = [1, 2, 2, 3, 3, 4, 5, 5, 99]

# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)

#     for number in unique_numbers:
#         if number == number:
#             list_of_unique_numbers.append(number)
#         else:
#             continue

#     return list_of_unique_numbers

# print(get_unique_numbers(numbers))


