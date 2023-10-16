# Создайте класс окружность. Класс должен принимать радиус окружности 
# при создании экземпляра. 
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Round_sq:
    # свойства класса
    def __init__(self, rad): # атрибут класса
        self.rad = rad
    
    def length(self): # метод
        return 2*pi*self.rad
    
    def sq(self):
        return pi*self.rad**2
    
r1 = Round_sq(10)
print(r1.length())
print(r1.sq())