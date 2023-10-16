# Дорабатываем класс прямоугольник из прошлого семинара. 
# Добавьте возможность сложения и вычитания. При этом должен 
# создаваться новый экземпляр прямоугольника. Складываем и 
# вычитаем периметры, а не длинну и ширину. 
# При вычитании не допускайте отрицательных значений.

class Rect:
    def __init__(self, lenght, width=None):
        self.l = lenght
        if width:
            self.w = width
        else:
            self.w = lenght

    def per(self):
        return 2 * (self.l + self.w)

    def sq(self):
        return self.l * self.w

    def __add__(self, other: "Rect"):
        if self.w == other.w:
            sum_per = self.per() + other.per()
            new_len = sum_per/2 - self.w
            return Rect(new_len, self.w)
        else:
            raise ValueError
        
    def __sub__(self, other: "Rect"):
        if self.w == other.w:
            sum_per = self.per() - other.per()
            new_len = sum_per/2 - self.w
            return Rect(new_len, self.w)
        else:
            raise ValueError
        
    def __repr__(self) -> str:
        return f"Rect({self.l}, {self.w})"
        
x1 = Rect(3, 2)
x2 = Rect(3, 2)
print(x1)
print(x2)

a = x1 - x2
print(a)