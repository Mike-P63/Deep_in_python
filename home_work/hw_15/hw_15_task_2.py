
import logging
import time
from datetime import datetime

FORMAT = '{levelname}, {asctime}, {msg}'

logging.basicConfig(format = FORMAT, style='{', filename = "myfunc_3.log", filemode ="w", encoding="utf-8", level=logging.ERROR)
logger = logging.getLogger(__name__)

def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}")
        return None
    return wrapper

@ log_dec
class MyStr(str):
    """
    Класс для создания строки с информацией об авторе и времени создания.

    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.

    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.

    """

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"

event = MyStr()   # Создаем ошибку, намеренно не передавая аргументы
print(event)

my_string = MyStr()  # # Создаем ошибку, намеренно не передавая аргументы
print(my_string)

# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))