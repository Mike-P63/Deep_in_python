# Создайте модуль и напишите в нём функцию, которая получает 
# на вход дату в формате DD.MM.YYYY и возвращает истину, если 
# дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. Проверку года на 
# високосность вынести в отдельную защищённую функцию.

# __all__ = ['check_date', '_leap_ear']

def check_date(date:str)->bool:
    day, mounth, year = map(int, date.split('.'))
    if _leap_ear(year) and mounth == 2:
        return 1 <= day <= 29
    return 1 <= day <= 31 and 1 <= mounth <= 12 and 1 <= year <= 9999
    

def _leap_ear(year):
    return year%4 ==0 and year%100 != 0

if __name__ == "__main__":
    print(check_date(input()))

# def date_to_prove(date:str)->bool:
#     day, month, year = map(int, date.split('.'))
#     if 1 <= year <= 9999:
#         if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
#             return True
#         elif month in [4, 6, 9, 11] and 1 <= day <= 30:
#             return True
#         elif 1 <= day <= 28:
#             return True
#         else:
#             return False
#     return False
    
# print(date_to_prove(input()))