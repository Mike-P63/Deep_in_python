
# Напишите программу, которая решает квадратные уравнения
# даже если дискриминант отрицательный. Используйте комплексные
# числа для извлечения квадратного корня.

a = 5
b = 8
c = -20
d = b ** 2 - 4 * a * c

# деление не возвращает int

x1 = (- b + d ** 0.5)/2*a
x2 = (- b - d ** 0.5)/2*a

print(x1, x2)
print(type(x1), type(x2))
