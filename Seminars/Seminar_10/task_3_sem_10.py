# Напишите класс для хранения информации о человеке: 
# ФИО, возраст и т.п. на ваш выбор. У класса должны быть 
# методы birthday для увеличения возраста на год, full_name 
# для вывода полного ФИО и т.п. на ваш выбор. Убедитесь, что 
# свойство возраст недоступно для прямого изменения, но есть 
# возможность получить текущий возраст.



class Person:
    def __init__(self, name, second_name, patronymic,age):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age+=1

    def fio(self):
        return f"{self.name}{self.second_name}{self.patronymic}{self.__age}"
    
person1 = Person("Ivan", "Ivanov", "Ivanovich", 44)

print(person1.fio())
person1.birthday()
print(person1.fio())
person1.__age = 45
print(person1.fio())

