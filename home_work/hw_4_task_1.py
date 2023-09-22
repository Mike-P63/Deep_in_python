# Напишите функцию для транспонирования матрицы. 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


matrix = [[1, 2, 3], [4, 5, 6]]
matrix_transpond = list(map(list, zip(*matrix)))
print(f"Исходная матрица размером 2*3: {matrix}")
print(f"Транспонированная матрица размером 3*2: {matrix_transpond}")


# Решение через цикл c генератором:

matrix_1 = [[1, 2, 3], [4, 5, 6]]
transpond_matrix = [[0 for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        transpond_matrix[j][i] = matrix_1[i][j]
print(transpond_matrix)
