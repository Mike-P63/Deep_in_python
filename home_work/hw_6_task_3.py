# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка 
# ферзей на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи 
# размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

import random

# def random_queens_placement():
#     board = [[0] * 8 for _ in range(8)]
#     for row in range(8):
#         col = random.randint(0, 7)
#         board[row][col] = 1
#     return board

# for _ in range(4):
#     board = random_queens_placement()
#     for row in board:
#         print(row)


def random_queens_placement(positions):
    for i in range(8):
        for j in range(i+1, 8):
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True

def generate_positions():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not random_queens_placement(positions):
            random.shuffle(positions)
        print(positions)


print(generate_positions())