n = int(input('Введите кол-во школьников:'))
k = int(input('Введите кол-во яблок:'))
print(f'{k} //{n} = {k // n}')
print(f'{k} % {n} = {k % n}')
a = int(input('Кол-во учеников в классе - а:'))
b = int(input('Кол-во учеников в классе - b:'))
c = int(input('Кол-во учеников в классе - c:'))
print(f'{a} + {b} + {c} = {a + b + c}')
print(f'Необходимое кол-во парт: {(a + b + c) // 2 + (a + b + c) % 2}')
seconds = int(input('Кол-во прошедших секунд с начала суток:'))
print(f'Время {seconds // 3600}:{(seconds - 3600 * (seconds // 3600)) // 60}:{seconds % 60}')
number = int(input('Введите целое трехзначное число:'))
print(number % 10,number // 10 % 10,number // 100)