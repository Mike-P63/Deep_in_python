# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква
# в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ,
# а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не
# совпадают в ваших решениях.

a = "Введите строку"

result = {}
result1 = {}

for i in a:
    result[i] = result.get(i, 0)+1
print(result)

for i in a:
    if i not in result1:
        result1[i] = a.count(i)
print(result1)