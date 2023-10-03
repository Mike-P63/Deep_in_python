from tasks_sem_and_hw import hw_7_task_1 as hw

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге experemental_files")
    files_renamed = hw.group_rename_files("_fn_", ".txt", path = None)  # Изменение файлов, созданных на семинаре в корневом каталоге
    print(f"Переименовано: {files_renamed}") # В принте "Переименовано: 8"