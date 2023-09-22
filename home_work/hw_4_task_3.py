# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

from datetime import date

summa_start = 0
count = 0
list_operation = []
RICHLIMIT = 5_000_000
RICHTAX = 0.1
THREEOPERATIONS = 3
PERCENT_ADD = 0.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600


def add_money(cash: float) -> None:
    global summa_start
    global count
    summa_start += cash
    count += 1
    if count % THREEOPERATIONS == 0:
        summa_start = summa_start + PERCENT_ADD * summa_start
        print("На Ваш счет зачислены проценты в размере: ", PERCENT_ADD * summa_start)


def take_money(cash: float) -> None:
    global summa_start
    global count
    summa_start -= cash
    count += 1
    if cash * COMMISSIONOUTDROW < MINLIMIT:
        summa_start -= MINLIMIT
        print("С Вашего счета списаны проценты за cash: ", MINLIMIT)
    elif cash * COMMISSIONOUTDROW > MAXLIMIT:
        summa_start -= MAXLIMIT
        print("С Вашего счета списаны проценты за cash: ", MAXLIMIT)
    else:
        summa_start -= cash * COMMISSIONOUTDROW
        print("С Вашего счета списаны проценты за cash: ", cash * COMMISSIONOUTDROW)
    if count % THREEOPERATIONS == 0:
        summa_start = summa_start + COMMISSIONOUTDROW * summa_start
        print("На Ваш счет начислены проценты в размере: ", COMMISSIONOUTDROW * summa_start)


def check_summa_deposit() -> int:
    while True:
        cash = int(input("Введите сумму наличных кратно 50:\n"))
        if cash % FREENDERING == 0:
            return cash


def exit_bank():
    print("Баланс = ", summa_start)
    print("Спасибо за обращение в Наш банк! Будем рады видеть Вас снова!\n")
    exit()


while True:
    action = input("1 - снять деньги\n2 - пополнить счет\n3 - баланс счета\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if summa_start > RICHLIMIT:
            summa_start = summa_start - summa_start * RICHTAX
            print("С Вашего счета списан налог на богатство: ", summa_start * RICHTAX)
        
        cash = check_summa_deposit()
        if cash < summa_start:
            take_money(cash)
            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Денег на счете нет\n")
        print("Баланс = ", summa_start)
    elif action == '2':
        cash = check_summa_deposit()
        add_money(cash)
        if summa_start > RICHLIMIT:
            summa_start = summa_start - summa_start * RICHTAX
            print("С Вашего счета списан налог на богатство: ", summa_start * RICHTAX)
        print("Баланс = ", summa_start)
        list_operation.append([str(date.today()), cash])
    elif action == '3':
        print("Баланс = ", summa_start)
    elif action == '4':
        print(list_operation)
        print("Баланс = ", summa_start)
    else:
        exit_bank()
        