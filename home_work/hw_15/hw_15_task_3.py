# Работаю с логгированием и парсером без создания функции для него

import argparse
import logging

FORMAT = '{levelname}, {asctime}, {msg}'

logging.basicConfig(format = FORMAT, style='{', filename = "myfunc_4.log", filemode ="w", encoding="utf-8", level=logging.ERROR)
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
class Matrix:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
       
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

matrix1 = Matrix()  # намеренно не передаем аргументы в функцию
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2,3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param', metavar='rows cols', type=int, nargs=2, help='enter param separated by a space')
    args = parser.parse_args()
    print(Matrix(*args.param))


# Выводим матрицы
print(matrix1)

print(matrix2)

# Ввод в командной строке: python Home_Work/hw_15/hw_15_task_3.py 2 3

# В файле myfunc_4.log:
# ERROR, 2023-11-01 14:29:27,295, Ошибка Matrix.__init__() missing 2 required positional arguments: 'rows' and 'cols' в функции Matrix при аргументах (), {}
