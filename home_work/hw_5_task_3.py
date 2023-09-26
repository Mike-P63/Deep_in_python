# Создайте функцию генератор чисел Фибоначчи fibonacci.

# def fibonacci(limit: int):
#     fibo = [0, 1]
#     while limit > 0:
#         yield fibo[-1]
#         fibo.append(fibo[-1] + fibo[-2])
#         limit -= 1

# f = fibonacci(10)
# for i in range(10):
#     print(next(f))

# def fibonacci(number: int) -> (iter, int):
#     fibo_list = [0, 1, 1]
#     current_number = 0
#     while current_number < number:
#         while len(fibo_list) < number:
#             fibo_list.append(sum(fibo_list[-2:]))
#         yield fibo_list[current_number]
#         current_number += 1
        
# f = fibonacci(10)
# for i in range(10):
#     print(next(f))

# def fibonacci(n):
#     a, b = 0, 1
#     for __ in range(n):
#         yield a
#         a, b = b, a + b

# f = fibonacci(10)
# for i in range(10):
#     print(next(f))


def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b

f = fibonacci()
for i in range(10):
    print(next(f))