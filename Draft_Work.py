
number = int(input('Введите любое число для проверки:'))
if number == 2 or number == 3:
    print('Простое число')
elif number % 2 != 0 and number % 3 != 0:
    print('Простое число')
else:
    print('Сложное число')
