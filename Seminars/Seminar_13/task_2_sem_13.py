# Создайте функцию аналог get для словаря. Помимо самого словаря функция 
# принимает ключ и значение по умолчанию. При обращении к несуществующему 
# ключу функция должна возвращать дефолтное значение. 
# Реализуйте работу через обработку исключений.


def my_func(storage, key, value = None):
    try:
        return storage[key]
    except KeyError:
        return value
    

f = {'f' : '1', 'd' : '3', 's' : '5'}
print(my_func(f, 's', 23))