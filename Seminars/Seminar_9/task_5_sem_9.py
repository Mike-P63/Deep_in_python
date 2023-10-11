# Объедините функции из прошлых задач. Функцию угадайку
# задекорируйте декораторами для сохранения параметров,
# декоратором контроля значений и декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from task_2_sem_9 import game_decor
from task_3_sem_9 import func_dec
from task_4_sem_9 import func_count


@func_count(3)
@func_dec
@game_decor
def guess(rnd_num, count_num):
        for i in range(count_num):
            input_num = int(input("Введите число для угадывания: "))
            if input_num > rnd_num:
                print("Число меньше загаданного")
            elif input_num < rnd_num:
                print("Число больше загаданного")
            else:
                print(rnd_num)
                return True
        return False

if __name__ == "__main__":
    print(guess(2,3))