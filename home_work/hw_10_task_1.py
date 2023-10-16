# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы 
# (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса.
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров. 
# Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal'). *args - переменное количество аргументов, 
# представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости 
# от типа животного. Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         return "Myau"


# animals_dict = {"Animal": Animal}
# type_a = "Animal"
# name_a = "Den"

# new_an = animals_dict[type_a](name_a)
# print(new_an)
# print(new_an.make_sound())


# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         self.wingspan = wingspan
#         self.name = name

#     def wing_length(self, name, wingspam):
#         self.wingspan = wingspam
#         self.name = name
#         return f'{wingspam/2}'
    
# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         self.max_depth = max_depth
#         self.name = name
    
#     def depth(self, max_depth, smalldepth, middledepth, highdepth):
#         self.max_depth = max_depth
#         self.smalldepth = smalldepth
#         self.middledepth = middledepth
#         self.highdepth = highdepth
        
#         return {}
    
# class Mammal(Animal):
#     def __init__(self, name, weigth):
#         self.weigth = weigth
#         self.name = name
#     def category(self, weigth, small, usual, giant):
#         self.weigth = weigth
#         self.small = small
#         self.usual = usual
#         self.giant = giant
#         return {}

# class AnimalFactory:
#     def create_animal(self, animal_type, *args):
#         if animal_type == "Bird":
#             return Bird.wing_length
        # elif animal_type == "Fish":
        #     return Fish.depth
        # elif animal_type == "Mammal":
        #     return Mammal.category
        # else:
        #     raise ValueError("Invalid animal type")

# Создание экземпляров животных
# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# Вывод результатов
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())


# Вывод:

# 100.0
# Средневодная рыба
# Гигант


# class Cat:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def speak(self):
#         return "Meow"

# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def speak(self):
#         return "Woof"

# class AnimalFactory:
#     def create_animal(self, animal_type, name, breed, age):
#         if animal_type.lower() == "cat":
#             return Cat(name, breed, age)
#         elif animal_type.lower() == "dog":
#             return Dog(name, breed, age)
#         else:
#             raise ValueError("Invalid animal type")
        
# # Использование класса
# factory = AnimalFactory()

# cat = factory.create_animal("cat", "Fluffy", "Persian", 3)
# dog = factory.create_animal("dog", "Buddy", "Golden Retriever", 5)

# print(cat.speak())  # Выводит: "Meow"
# print(dog.speak())  # Выводит: "Woof"






# class AnimalFabric:
#     def make_animal(self, animal_type: str, *args, **kwargs):
#         new_animal = self._get_maker(animal_type)
#         return new_animal(*args, **kwargs)

#     def _get_maker(self, animal_type: str):
#         types = {"dog": Dog, "cat": Cat, "fish": Fish}
#         return types[animal_type.lower()]


# if __name__ == '__main__':
#     fabric = AnimalFabric()
#     animal_from_fabric = fabric.make_animal("dog", "Bobik", "Retriver")
#     animal_from_fabric.commands = ["сидеть", "служить"]
#     print(animal_from_fabric)




class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(Animal):

    def __init__(self, name: str, age: int, hair: str, voice: str, color: str):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Hair:":8}{self.hair}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}\n'
                )
class AnimalFabric:

    def __init__(self, animal_class: str,  **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'voice':
                self.voice = value
            if key == 'hair':
                self.hair = value

    def get_info_animal(self):
        if self.animal_class == 'bird':
            return Bird(self.name, self.age, self.color, self.voice)
        elif self.animal_class == 'mammal':
            return Mammal(self.name, self.age, self.hair, self.voice, self.color)
        elif self.animal_class == 'fish':
            return Fish(self.name, self.age, self.color)
        else:
            return f'нет такого животного'



animal1 = AnimalFabric(animal_class='bird', name='ворона', age=3, color='серая', voice='кар-кар').get_info_animal()
print(animal1.get_info())

animal2 = AnimalFabric(animal_class='mammal', name='собака', age=10, hair='короткая шерсть', voice='гав-гав', color='серый').get_info_animal()
print(animal2.get_info())