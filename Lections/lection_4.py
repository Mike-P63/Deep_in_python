# def quadratic_equations(a: int | float, b: int | float, c: int |float) -> tuple[float, float] | float | None:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return None

# print(quadratic_equations(2, -3, -9))


def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    return data

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')
print()



# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data

def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

#  функция принимает любое число позиционных аргументов

def mean(*args):
    return sum(args) / len(args)
print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))

# Параметр **kwargs работает аналогично, но принимает ключевые параметры

def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')
    
print(school_print(химия=5, физика=4, математика=5, физра=5))


# Один из случаев когда обращение из тела функции к глобальной переменной
# считается нормальным — доступ к константам.

LIMIT = 1_000
def func(x, y):
    result = x ** y % LIMIT
    return result
print(func(42, 73))


# Анонимные функции, они же лямбда функции — синтаксический сахар для обычных
# питоновских функций с рядом ограничений. Они позволяют задать функцию в одну
# строку кода без использования других ключевых слов.

def add_two_def(a, b):
    return a + b

add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

# Правильное применение функции лямбда

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')

# Документирование функции

def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.

    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m

print(max_before_hundred(-42, 73, 74, 256, 0))
help(max_before_hundred)

# Функции из коробки

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)
print()

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)
print()

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary* award:.2f}')

print()

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))
print()

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))
print()

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

print()

# Функции chr(), ord()

print(chr(97))
print(chr(1105))
print(chr(128519))
print()

print(ord('a'))
print(ord('а'))
print(ord('😉'))
print()

# Функции locals(), globals(), vars()

SIZE = 10

# def func(a, b, c):
#     x = a + b
#     print(locals())
#     z = x + c
#     return z

# func(1, 2, 3)
# print()

data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))

# print(*filter(lambda x: not x[0].startswith('__'),
# globals().items()))
