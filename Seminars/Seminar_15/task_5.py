# Дорабатываем задачу 4. Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.


import argparse
import datetime

from task_3 import log_dec

# MONTH = {"января":1, "февраля":2,"марта":3,"апреля":4,"мая":5,
#          "июня":6,"июля":7,"августа":8, "сентября":9, "октября":10,"ноября":11,"декабря":12}

# MONTHREV = dict(map(lambda x: (x[1], x[0]), MONTH.items()))
       

# WEEKDAY = {"понедельник":1, "вторник":2,"среда":3,"четверг":4,"пятница":5,
#          "суббота":6,"воскресенье":7,}

# @log_dec
# def print_date(str_day):
#     num, weekday, month = str_day.split()
#     num = int(num[0])
#     weekday = WEEKDAY[weekday]-1
#     month = MONTH[month]
#     count = 0
#     for i in range(1,32):
#         temp_date = datetime.datetime(datetime.datetime.now().year,month, i)
#         if temp_date.weekday() == weekday:
#             count+=1
#             if count == num:
#                 return temp_date
#     raise ValueError


# def par():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-n' default=1, )
#     parser.add_argument('-v', default=)

# print(MONTHREV)
# print(print_date('77-й четверг ноября'))


MOUTH = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
         "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}

MOUTHREV = dict(map(lambda x: (x[1], x[0]), MOUTH.items()))

WEEKDAY = {"понедельник": 1, "вторник": 2, "среда": 3,
           "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}

WEEKDAYREV = dict(map(lambda x: (x[1], x[0]), WEEKDAY.items()))


@log_dec
def print_date(str_day):
    num, weekday, month = str_day.split()
    num = int(num[0])
    weekday = WEEKDAY[weekday] - 1
    month = MOUTH[month]
    count = 0
    for i in range(1, 32):
        temp_date = datetime.datetime(datetime.datetime.now().year, month, i)
        if temp_date.weekday() == weekday:
            count += 1
            if count == num:
                return temp_date
            

    raise ValueError


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=1)
    parser.add_argument(
        '-w','--weekday', default=WEEKDAYREV.get(datetime.datetime.now().weekday(), "понедельник"))
    parser.add_argument(
        '-m','--month', default=MOUTHREV.get(datetime.datetime.now().month, "января"))
    args = parser.parse_args()
    return print_date(f'{args.number}-ый {args.weekday} {args.month}')

print(par())


# Seminars/Seminar_15/task_5.py -n 1 -w воскресенье -m октября