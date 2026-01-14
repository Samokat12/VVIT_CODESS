from saasdas import stepeniya
from saasdas import numbers


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(f'Число {number1} в степени {number2} равно={stepeniya.stepeniya(number1,number2)}')
print(f"Произведение чисел равно={numbers.numbers(number1,number2)}")