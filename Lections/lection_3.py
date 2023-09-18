

my_list = [1, 9, 5, 17, 6, 22, 35, 22, 5]
print(my_list)
my_list.append(77)
print(my_list)
n = [22, 35, 89, 100]
my_list.extend(n)
print(my_list)
my_list.pop(1)
print(my_list)
print(my_list.count(22))
spam = my_list.index(1)
print(spam)
eggs = my_list.index(5, spam +1, 90)
print(eggs)
my_list.insert(2,444)
print(my_list)
my_list.remove(444)
print(my_list)
sort_list = sorted(my_list)
print(sort_list)
print()

rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
print()

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print()

my_list2 = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list2)
print(type(res), res)
rev_list = list(reversed(my_list2))
print(rev_list)
print()

my_list3 = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list3[2:7:2])
print(my_list3[:7:2])
print(my_list3[2::2])
print(my_list3[2:7:])
print(my_list3[8:3:-1])
print(my_list3[3::])
print(my_list3[:7:])
print()

my_list4 = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list4
print(my_list4, new_list, sep='\n')
my_list4[2] = 555
print(my_list4, new_list, sep='\n')
print()

my_list5 = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list5.copy()
print(my_list5, new_list, sep='\n')
my_list5[2] = 555
print(my_list5, new_list, sep='\n')
print()

import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
print()

my_list6 = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(my_list6))
print(len(matrix))
print(len(matrix[1]))
print()

# STR

text = 'Hello world!'
print(text[6])
print(text[3:7])
new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))
print()
text = 'Hello world!'
print(text[::-1])
print()

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)
print()

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)
print()

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)
print()

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')
print()

# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

# a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()
# print(a,b,c)

text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print()

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))
print()

my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))
print()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

numbers = [23, 23, 38, 38, 66, 66, 90]

def get_dubble_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
print(get_dubble_numbers(numbers))