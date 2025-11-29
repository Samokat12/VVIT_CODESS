path = 'Lab_3./example.txt'

def func(path, method):
    if method == 'целиком':        
        with open(path, 'r') as file:
            content = file.read()
        return content
 
    elif method == 'построчно':
        with open(path, 'r') as file:
                return [line.strip() for line in file]
 
    else:
        return('Ошибка!') 
                  
method = input('Какой формат чтения вы хотите выбрать?\nчтение целиком или построчно?: ')
print(func(path, method))