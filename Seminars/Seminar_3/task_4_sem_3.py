
# Создайте вручную список с повторяющимися элементами. 
# Удалите из него все элементы, которые встречаются дважды.


a = [1, 2, 3, 1, 2, 5, 7, 5, 33, 33, 8, 8, 9, 9]
for i in set(a):
    if a.count(i) == 2:
        a.remove(i)
        a.remove(i)
print(a)