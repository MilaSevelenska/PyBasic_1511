a = float(input('Ввести операнд 1:'))
b = float(input('Ввести операнд 2:'))
user_choice = input('Выбрать действие:')
# Два варианта калькулятора - или или
if user_choice == '+':
    print(a + b)
    print(f'{a} + {b} = {a + b}')
elif user_choice == '-':
    print(a - b)
    print(f'{a} - {b} = {a - b}')
elif user_choice == '/':
    print(a / b)
    print(f'{a} / {b} = {a / b}')
elif user_choice == '*':
    print(a * b)
    print(f'{a} * {b} = {a * b}')
elif user_choice == '**':
    print(a ** b)
    print(f'{a} ** {b} = {a ** b}')
else:
    print()
number = int(input('Ввести целое число N:'))
for i in range(1, number):
  if number >= i ** 2:
    print(i ** 2, end=' ')
print()
number = int(input('Введите любое число для проверки:'))
if number == 2 or number == 3:
    print('Простое число')
elif number % 2 != 0 and number % 3 != 0:
    print('Простое число')
else:
    print('Сложное число')
K = int(input('Введите кол-во грибов K:'))
if K % 10 == 1:
    print(f'Маша нашла в лесу {K} гриб')
elif K % 10 == 2:
    print(f'Маша нашла в лесу {K} гриба')
elif K % 10 == 3:
    print(f'Маша нашла в лесу {K} гриба')
elif K % 10 == 4:
    print(f'Маша нашла в лесу {K} гриба')
elif K % 10 == 0:
    print(f'Маша нашла в лесу {K} грибов')
elif K % 10 == 5:
    print(f'Маша нашла в лесу {K} грибов')
elif K % 10 == 6:
    print(f'Маша нашла в лесу {K} грибов')
elif K % 10 == 7:
    print(f'Маша нашла в лесу {K} грибов')
elif K % 10 == 8:
    print(f'Маша нашла в лесу {K} грибов')
elif K % 10 == 9:
    print(f'Маша нашла в лесу {K} грибов')
else:
    print()