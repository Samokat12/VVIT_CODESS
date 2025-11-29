def text(write):
    try:
        if write == 'целиком':
            with open('Lab_3/example.txt', 'r', encoding='utf-8') as file:
                return file.read()
        elif write == 'построчно':
            with open('Lab_3/example.txt', 'r', encoding='utf-8') as file:
                return [line.strip() for line in file]
        else:
            return 'Ошибка!'
    except FileNotFoundError:
        return 'Ошибка: Файл не найден!'
write = input('Какой формат чтения вы хотите выбрать?\nчтение целиком или построчно?: ')
print(text(write))