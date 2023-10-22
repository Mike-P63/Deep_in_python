
class Archive:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.archive_text = []
            cls.instance.archive_number = []
        else:
            cls.instance.archive_text.append(cls.instance.text)
            cls.instance.archive_number.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number
            
    def __str__(self):
        return f' Text is {self.text} and number is  {self.number}. Also [{self.text}] and [{self.number}]'

    def __repr__(self):
        return f' Text is {self.text} and number is {self.number}. Also [{self.text},{self.text}] [{self.number},{self.number}]'


archive1 = Archive("Запись 1", 42)
print(archive1)
archive2 = Archive("Запись 2", 3.14)
print(archive2)




# a = Archive('yhhjjjkklll', 5)
# print(a.archive_text, a.archive_number)
# b = Archive('uytuitiu', 4)
# print(b.archive_text, b.archive_number)
# print(a.archive_text, a.archive_number)
# print(Archive.__doc__)