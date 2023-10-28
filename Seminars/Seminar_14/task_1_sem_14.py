# Создайте функцию, которая удаляет из текста все символы кроме 
# букв латинского алфавита и пробелов. 
# Возвращается строка в нижнем регистре.


# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов


from string import ascii_letters


def remove_char(text):
    """
    >>> remove_char('qwerty')
    'qwerty'
    >>>
    >>> remove_char('QWERTY')
    'qwerty'
    >>> remove_char('qwerty,UUU,.')
    'qwertyuuu'
    >>> remove_char('ываываывапэ')
    ''
    """
    new_text = []
    for el in text.lower():
        if el in ascii_letters + ' ': 
            new_text.append(el)
    return ''.join(new_text)

# r = remove_char('dh eффв вОРЫS WE')
# print(r)

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)