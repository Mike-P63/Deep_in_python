
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и 
# heck_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не 
# били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а 
# если бьют - ложь. Не забудьте напечатать результат.




# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# False
# queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
# False
# queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
# False
# queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
# False
# queens = []
# True
# queens = [(4, 4)]
# True

# def is_attacked(x1,y1,x2,y2):
#     if x1==x2 or y1==y2 or abs(x1-x2) == abs(y1-y2):
#         return True
#     return False

# def check_queens(queens):
#     for i in range(len(queens)):
#         for j in range(i+1, len(queens)):
#             x1, x2 = queens[i]
#             y1, y2 = queens[j]
#             if is_attacked(x1,y1,x2,y2):
#                 return True
#     return False

# print(check_queens(queens))
    

def check_queens(queens):
    for i in queens:
        for j in queens:
            if i[0] == j[0] and i[1] == j[1]:
                continue
            elif abs(i[0]-j[0]) == abs(i[1]-j[1]) or i[0] == j[0] or i[1]==j[1]:
                return False
    else:
        return True
    
# print(check_queens(queens))

print(check_queens(queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))
print(check_queens(queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]))
print(check_queens(queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]))
print(check_queens(queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]))
print(check_queens(queens = []))
print(check_queens(queens = [(4, 4)]))