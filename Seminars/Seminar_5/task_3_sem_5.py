# Продолжаем развивать задачу 2. Возьмите словарь, который вы получили. 
# Сохраните его итераторатор. 
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

a = "qwerty"
new_gen = {i:ord(i) for i in a}
print(new_gen)

new_iter = iter(new_gen.items())

for i in range(5):
    print(next(new_iter))