# from collections import defaultdict


# class Storage:
#     def __init__(self):
#         self.storage = defaultdict(list)
#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in
#         self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'

#     def __call__(self, value):
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'

# s = Storage()
# print(s(42))
# print(s(72))
# print(s('Hello world!'))
# print(s(0))
# print(s)


#  пример:

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b})'
#     def __call__(self, *args, **kwargs):
#         self.a.append(args)
#         self.b.update(kwargs)
#         return True

# x = MyClass([42], {73: True})
# y = x(3.14, 100, 500, start=1)
# x(y=y)
# print(x)


#  Итераторы

# class Fibonacci:
    
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.first < self.stop:
#                 self.first, self.second = self.second, self.first + self.second
#                 if self.start <= self.first < self.stop:
#                     return self.first
#         raise StopIteration
    
    
# fib = Fibonacci(20, 100)
# for num in fib:
#     print(num)

# Пример менеджера контекста:

# import sqlite3


# class DB:
#     def __init__(self, name):
#         self.name = name
#         self.connection = None
#         self.cursor = None
        
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.name)
#         self.cursor = self.connection.cursor()
#         return self.cursor
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.commit()
#         self.connection.close()
#         self.cursor = self.connection = None
#         db = DB('sqlite.db')
    
#     with db as cur:
#         cur.execute("""create table if not exists users(name,
#     age);""")
#         cur.execute("""insert into users values ('Гвидо', 66);""")