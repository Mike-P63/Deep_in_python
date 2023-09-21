# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого 
# символа введённой строки отсортированный по убыванию.

# def text_ord(n:str)->list[int]:
#     d = []
#     for el in n:
#         d.append(ord(el))
#     return sorted(list(set(d)), reverse=True)

# n = input()
# print(text_ord(n))


def text_ord(n:str)->list[int]:
    d = set()
    for el in n:
        d.add(ord(el))
    return sorted(list(d), reverse=True)

n = input()
print(text_ord(n))


# def str_ord(n: str) -> list[int]:
#     return sorted(list(set(map(ord, list(n)))), reverse=True)

# print(str_ord(input()))