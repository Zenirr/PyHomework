# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = input('Введите натуральное число = ')
numbers = []
j = 2
while 1:
    if number % j == 0:
        numbers.append(j)
        number /= j
        j = 2
    elif number == 1:
        break
    else:
        j += 1

if len(numbers) == 1:
    print('Число простое')
else:
    print(f'Простые числа: {numbers}')