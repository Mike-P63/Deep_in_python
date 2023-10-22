
import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.datetime.today()
        date = datetime.datetime.today()
        a = date.strftime('%Y-%m-%d %H:%M')
        return instance
     
    def __init__(self, value, author):
        self.value = value
        self.author = author
        date = datetime.datetime.today()
        a = date.strftime('%Y-%m-%d %H:%M')

    def __str__(self):
        date = datetime.datetime.today()
        a = date.strftime('%Y-%m-%d %H:%M')
        return f' {self.value} (Автор:  {self.author}, Время создания: {a})'

    def __repr__(self):
        date = datetime.datetime.today()
        a = date.strftime('%Y-%m-%d %H:%M')
        return f"MyStr({self.value}, {self.author})"

event = MyStr('Завершилось тестирование', 'John')
print(event)

# my_string = MyStr("Пример текста", "Иван")
# print(my_string)

# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))


