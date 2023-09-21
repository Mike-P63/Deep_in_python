# Функция получает на вход список чисел. Отсортируйте его элементы 
# in place без использования встроенных в язык сортировок. Как вариант 
# напишите сортировку пузырьком. Её описание есть в википедии.


def sort_list(list_: list[int]):
    for i in range(len(list_)):
        for j in range(len(list_)-1):
            if list_[i]>list_[j]:
                list_[i], list_[j] = list_[j], list_[i]

list_ = [12, 10, 22, 44, 88, 124]
sort_list(list_)
print(list_)


