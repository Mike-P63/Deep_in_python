# Создайте класс прямоугольник. Класс должен принимать длину и ширину 
# при создании экземпляра. У класса должно быть два метода, возвращающие 
# периметр и площадь. Если при создании экземпляра передаётся только одна сторона, 
# считаем что у нас квадрат.

class Rect:
    def __init__(self, length, width = None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def per(self):
        return 2*(self.length + self.width)
    
    def sq(self):
        return self.length*self.width
    
l1 = Rect(3,2)
l2 = Rect(3)

print(l1.per(), l1.sq())
print(l2.per(), l2.sq())