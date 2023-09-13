# Напишите программу, которая запрашивает год и проверяет его на високосность. 
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print



# year = int(input('Enter year: '))
# if year%4 != 0 or year%100 == 0 and year%400 !=0:
#      print('Usual year')
# else:
#      print('VISOKOSNIY')

MAIN_DEVIDER = 4
EXEPTION_DEVIDOR = 100
ADDITIONAL_DEVIDER =400

year = int(input('Enter year: '))
if year%MAIN_DEVIDER != 0 \
or year%EXEPTION_DEVIDOR == 0 \
and year%ADDITIONAL_DEVIDER !=0:
     print('Usual year')
else:
     print('VISOKOSNIY')