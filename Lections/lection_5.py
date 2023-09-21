# link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
# prefix, *_, suffix = link.split('/')


# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, end='\t')
# print()
# print(*data, sep='\t')

# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')
print()
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# for item in mult:
#     print(f'{item = }')

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
print()

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
print()

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)
print()


# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result

# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

print()

def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
    
for item in gen(10, 1):
    print(f'{item = }')