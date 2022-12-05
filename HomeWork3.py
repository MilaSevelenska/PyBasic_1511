a = float(input('Ввести операнд 1:'))
b = float(input('Ввести операнд 2:'))
print(
    '''
    Сложение  '+'
    Вычетание '-'
    Деление   '/'
    Умножение '*'
    Возведение в степень '**'
    '''
)
user_choice = input('Выбрать действие:')
if user_choice == '+':
    print(f'{a} + {b} = {a + b}')
elif user_choice == '-':
    print(f'{a} - {b} = {a - b}')
elif user_choice == '/':
    print(f'{a} / {b} = {a / b}')
elif user_choice == '*':
    print(f'{a} * {b} = {a * b}')
elif user_choice == '**':
    print(f'{a} ** {b} = {a ** b}')
else:
    print()



