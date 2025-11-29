def text(write):
    if write == 'создать новый файл':
        with open('Lab_3/user_input.txt', 'w') as file:
            input1 = input('Введите текст который хотите записать: ')
            file.write(f"\n{input1}")
            return 'Файл создан и текст записан.'

    elif write == 'дополнить файл':
        with open('Lab_3/user_input.txt', 'a') as file:
            input1 = input('Введите текст для добавления: ')
            file.write(f"\n{input1}")
            return 'Текст добавлен в существующий файл.'

    else:
        return 'Ошибка ввода!'
        

write = input('Вы хотите создать новый файл или дополнить существующий?: ')
print(text(write))
