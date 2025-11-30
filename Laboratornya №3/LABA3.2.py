def choosemethod(path, method, input1):
        if method == 1:
            with open(path, 'w') as file:
                file.write(f"{input1}")
            return 'Файл создан и текст записан.'
        if method == 2:
            with open(path, 'a') as file:
                file.write(f"\n{input1}")
            return 'Текст добавлен в существующий файл.'
        else:
            return('Ошибка ввода!')


method = int(input('Выберите способ записи: \n 1. Создать новый файл\n 2. Добавить текст в существующий\n'))
path = input("Отлично, введите имя файла: ")
input1 = input('Введите текст который хотите записать: ')
print(choosemethod(path, method, input1))