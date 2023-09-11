# a = 1 
# b = 2
# print('Сумма переменных', a, 'и', b, 'равна: ', a+b)


# pvd = 'text'
# res = input('Input password: ')
# if res == pvd:
#     print('OK, YOU ARE WELCOME!!!')
#     my_math = int(input('2+2 = '))
#     if 2 + 2 == my_math:
#         print("You are the best!")
#     else:
#         print('Be careful!')
# else:
#     print('Access denied!')
# print("Finish")


# year = int(input('Enter year: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 !=0:
#     print('Usual year')
# else:
#     print('VISOKOSNIY')

data = 0
while data < 100:
    data +=3
    if data % 40 == 0:
        break
else:
    data += 5
print(data)