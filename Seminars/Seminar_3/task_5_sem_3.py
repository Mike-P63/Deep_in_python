# Создайте вручную список с повторяющимися целыми числами. 
# Сформируйте список с порядковыми номерами нечётных 
# элементов исходного списка. 
# Нумерация начинается с единицы.

a = [1,2,3,4,4,5,5,6,7,7,8,9,9]
new_a = []
for n, el in enumerate(a, start = 1):
    if el % 2  != 0:
        new_a.append(n)
print(new_a)