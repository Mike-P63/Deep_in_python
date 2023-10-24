# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию, выведите:

# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:

# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:

# Оценка должна быть целым числом от 2 до 5

# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.

# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
# Атрибуты класса:

# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

# Магические методы (Dunder-методы):

# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и вызывает метод

# load_subjects для загрузки предметов из файла.

# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.

# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История

# Методы класса:

# load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

# add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.

# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.

# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

# get_average_grade(self): Возвращает средний балл по всем предметам.

# Пример

# На входе:


# student = Student("Иван Иванов", "subjects.csv")

# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)

# student.add_grade("История", 5)
# student.add_test_score("История", 92)

# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")

# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")

# print(student)


# На выходе:


# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История


# import csv


# class NameDescriptor:
#     def __set_name__(self, owner, name):
#         self._name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self._name, None)

#     def __set__(self, instance, value):
#         if not value.istitle() or not value.isalpha():
#             raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
#         setattr(instance, self._name, value)

# # Основной класс

# class Student:
#     first_name = NameDescriptor()
#     middle_name = NameDescriptor()
#     last_name = NameDescriptor()

#     def __init__(self, first_name, last_name, middle_name, csv_path):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name

#         # Загрузка предметов из CSV файла

#         with open(csv_path, 'r') as file:
#             reader = csv.reader(file)
#             self.subjects = {row[0]: {"grades": [], "test_scores": []} for row in reader}

#     def add_grade(self, subject, grade):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден.")
#         if grade < 2 or grade > 5:
#             raise ValueError("Оценка должна быть от 2 до 5.")
#         self.subjects[subject]["grades"].append(grade)

#     def add_test_score(self, subject, score):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден.")
#         if score < 0 or score > 100:
#             raise ValueError("Результат теста должен быть от 0 до 100.")
#         self.subjects[subject]["test_scores"].append(score)

#     def get_average_test_score(self, subject):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден.")
#         scores = self.subjects[subject]["test_scores"]
#         return sum(scores) / len(scores) if scores else 0

#     def get_average_grade(self):
#         total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
#         return sum(total_grades) / len(total_grades) if total_grades else 0
    
    
# student = Student("Иван", "Иванов", "Иванович", "subjects.csv")

# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)

# student.add_grade("История", 5)
# student.add_test_score("История", 92)

# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")

# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")

# print(student)


# import csv
# from functools import reduce
# from pathlib import Path


# class Validate:
#     "Дескриптор на проверку в ФИО наличия первой заглавной буквы, а также что ФИО состоит только из букв"

#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)

#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)

#     def validate(self, value):
#         if not value.isalpha():
#             raise TypeError(f'Значение {value} должно содержать только буквы')
#         if not value.istitle():
#             raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


# class Student:
#     name = Validate()
#     second_name = Validate()
#     surname = Validate()
#     _lessons = None

#     def __init__(self, name: str, second_name: str, surname: str, lessons_file: Path):
#         self.name = name
#         self.second_name = second_name
#         self.surname = surname
#         self.lessons = lessons_file

#     @property
#     def lessons(self):
#         return self._lessons

#     @lessons.setter
#     def lessons(self, lessons_file: Path):
#         " Декоратор считывает с файла список предметов в словарь lessons"

#         self._lessons = {"lessons": {}}
#         with open(lessons_file, 'r', encoding='utf-8') as csv_file:
#             reader = csv.reader(csv_file)
#             for row in reader:
#                 self._lessons["lessons"][row[0]] = {"assessments": [], "test_results": [], "average_test": None}
#         self._lessons["middle_assessment"] = None
#         self._lessons["middle_test"] = None

#     def __call__(self, lesson: str, number: int, type_est: str = "lesson"):
#         "Метод для сохранения новой оценки по предмету/тесту"

#         if lesson not in self.lessons["lessons"].keys():
#             raise AttributeError("Нет такого предмета")
#         if type_est == "lesson":
#             if number < 2 or number > 5:
#                 raise ValueError("Оценка должна быть от 2 до 5")
#             self.lessons["lessons"][lesson]["assessments"].append(number)
#             self.lessons["middle_assessment"] = self.calculate_middle_estimate(self.lessons)
#         elif type_est == "test":
#             if number < 0 or number > 100:
#                 raise ValueError("Оценка должна быть от 0 до 100")
#             self.lessons["lessons"][lesson]["test_results"].append(number)

#             # средний бал по тестам по каждому предмету:
#             self.lessons["lessons"][lesson]["average_test"] = reduce(lambda x, y: x + y, self.lessons["lessons"][lesson]["test_results"]) / len(self.lessons["lessons"][lesson]["test_results"])
#             self.lessons['middle_test'] = self.calculate_middle_test(self.lessons)

#     @staticmethod
#     def calculate_middle_estimate(lessons: dict) -> float:
#         "Подсчет средней оценки по всем предметам"

#         all_estimates = []
#         [all_estimates.extend(lessons["lessons"][name]["assessments"]) for name in lessons["lessons"]]

#         return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

#     @staticmethod
#     def calculate_middle_test(lessons: dict) -> float:
#         "Подсчет среднего бала по тестам по всем предметам"

#         all_estimates = []
#         [all_estimates.extend(lessons["lessons"][name]["test_results"]) for name in lessons["lessons"]]

#         return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

#     def __repr__(self):
#         result = f'ФИО студента = {self.name} {self.second_name} {self.surname}\nСредняя оценка по всем предметам = {self.lessons["middle_assessment"]}\nСредний бал по всем тестам = {self.lessons["middle_test"]}\n'
#         result += "\nОценки по предметам:\n"

#         for key, value in self.lessons["lessons"].items():
#             result += f'{key} = {value["assessments"]}\n'
#         result += "\nТесты по предметам:\n"
#         for key, value in self.lessons["lessons"].items():
#             result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'

#         return result


# if __name__ == '__main__':
#     student_1 = Student("Михаил", "Евгеньевич", "Иванов", 'lessons.csv')
#     student_1("русский язык", 3)
#     student_1("русский язык", 5)
#     student_1("физика", 5)
#     student_1("математика", 5)
#     student_1("информатика", 35, "test")
#     student_1("математика", 99, "test")
#     student_1("химия", 50, "test")
#     student_1("химия", 4)
#     student_1("информатика", 4)
#     student_1("информатика", 40, "test")
#     print(student_1)

#     student_2 = Student("Сергей", "Петрович", "Козлов", Path('lessons.csv'))
#     student_2("русский язык", 4)
#     student_2("история", 5)
#     student_2("физика", 3)
#     student_2("математика", 5)
#     student_2("история", 40, "test")
#     student_2("история", 98, "test")
#     student_2("химия", 4)
#     student_2("информатика", 3)
#     student_2("информатика", 55, "test")
#     student_2("история", 55, "test")
#     print(student_2)


import csv


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - init(self, name, subjects_file): конструктор класса
    - setattr(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - getattr(self, name): получение значения атрибута
    - str(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)


    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент:{self.name}\nПредметы:{', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}
    
    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)
    
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)