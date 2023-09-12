# Нарисовать в консоли ёлку спросив у 
# пользователя количество рядов. 
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input('Сколько рядов у ёлки? '))
STAR = '*'
SPACE = ' '
count_spaces = rows - 1
count_stars = 1
for row in range(rows):
    print(SPACE * count_spaces + STAR * count_stars)
    count_spaces -= 1
    count_stars += 2
