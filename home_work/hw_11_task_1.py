
import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.datetime.today()
        return instance
    
    def __init__(self, value, author):
        self.value = value
        self.author = author
        

    def __str__(self):
        return f' {self.value} (Автор:  {self.author}, Время создания: {datetime.datetime.today()})'

    def __repr__(self):
        return f"MyStr({self.value}, {self.author})"

# event = MyStr('Завершилось тестирование', 'John')
# print(event)

my_string = MyStr("Пример текста", "Иван")
print(my_string)

# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))
